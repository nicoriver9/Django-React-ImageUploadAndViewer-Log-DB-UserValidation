import cx_Oracle
import base64
from decouple import config
from rest_framework import status
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
import os
from datetime import datetime
# Create your views here.

class GetAllImagesView(APIView):
    def get(self, request):
        try:            
            IMAGE_DIRECTORY = config('IMAGE_DIRECTORY')
            images_path = os.path.join(IMAGE_DIRECTORY)                        
            image_data_list = []
    
            for filename in os.listdir(images_path):
                image_path = os.path.join(images_path, filename)
                with open(image_path, 'rb') as img_file:
                    image_data = img_file.read()
                    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
                image_info = {
                    'name': filename,
                    'image_base64': image_base64
                }
                image_data_list.append(image_info)
    
            return Response(                
                image_data_list
            , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Error al obtener las imágenes',
                'desc': e
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()  
    serializer_class = ImageSerializer

# The `ImageUploadView` class is a view for uploading images using the Django REST Framework.
class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        
        IMAGE_DIRECTORY = config('IMAGE_DIRECTORY')

        try:
            # image_file = request.FILES['image']
            ip_address = request.META.get('REMOTE_ADDR')
            uploaded_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            name = request.data.get('name')

            image_data_base64 = request.data.get('image_base64')

            image_data = base64.b64decode(image_data_base64)

            image_size = len(image_data)
            
            user = request.data.get('user', 'unknown_user')
            service = request.data.get('service', 'unknown_service')

            # Validar el usuario contra la base de datos Oracle
            validation_result = self.validate_user_with_oracle(user, service)
            if not validation_result['valid']:
                return Response({
                    'error': 'User validation failed.',
                    'success' : 'false'
                    }, status=status.HTTP_400_BAD_REQUEST)

            # Obtener la extensión del archivo a partir del nombre
            _, ext = os.path.splitext(name)
            ext = ext.lower()  # Convertir la extensión a minúsculas

            # Validar la extensión y ajustarla si es necesario
            if ext not in ['.png', '.jpg', '.jpeg']:
                return Response({'error': 'Formato de imagen no compatible'}, status=status.HTTP_400_BAD_REQUEST)
            if ext == '.jpeg':
                ext = '.jpg'  # Cambiar .jpeg a .jpg    

            # if validation_result['valid']:
                # user_id = validation_result['user_id']

            log_file_name = datetime.now().strftime('%Y-%m-%d') + '.txt'
            log_file_path = os.path.join('logs', log_file_name)
    
            log_message = f"Image '{name}' uploaded at {uploaded_at} from IP {ip_address}. User: {user}, Service: {service}. Size: {image_size} bytes.\n"

            with open(log_file_path, 'a') as log_file:
                log_file.write(uploaded_at + " " + log_message + '\n')

            image_path = os.path.join(IMAGE_DIRECTORY, name)            # Guardar la imagen en el directorio 'media/images'

            image = base64.b64decode(image_data_base64)
            with open(image_path, 'wb') as img_file:
                img_file.write(image)

            # with open(image_path, 'wb') as destination:
                # for chunk in image_file.chunks():
                    # destination.write(chunk)

            return Response({
                # 'message': 'Image uploaded successfully.',
                'success': 'true',
                # 'user': user_id
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_message = str(e)
            log_file_name = datetime.now().strftime('%Y-%m-%d') + '.txt'
            log_file_path = os.path.join('logs', log_file_name)
            with open(log_file_path, 'a') as log_file:
                log_file.write(date + " " + error_message + '\n')

            return Response({
                'error': error_message,
                'success': 'false'
                }, status=status.HTTP_400_BAD_REQUEST)

    def validate_user_with_oracle(self, user, service):
        
        user_id = user;

        log_file_name = datetime.now().strftime('%Y-%m-%d') + '.txt'
        log_file_path = os.path.join('logs', log_file_name)
        
        DATABASE_ENGINE = config('ENGINE', default='XE')
        DATABASE_USER = config('DB_USER')
        DATABASE_PASSWORD = config('PASSWORD')
        DATABASE_HOST = config('HOST')
        DATABASE_PORT = config('PORT')
        DATABASE_NAME = config('NAME')

        try:
            # Establecer conexión con la base de datos Oracle
            conn = cx_Oracle.connect(
                f'{DATABASE_USER}/{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_ENGINE}'
            )
            # Crear un cursor
            cursor = conn.cursor()

            # Consulta SQL para validar el usuario
            query = f"""SELECT 
                    s_user_servicio.USER_ID,
                    s_user_servicio.s_user_servicio_id, 
                    S_ACCION_USER_SERVICIO.ACCION_ID 
                FROM
                    s_user_servicio    
                    INNER JOIN S_ACCION_USER_SERVICIO ON s_user_servicio.S_USER_SERVICIO_ID = S_ACCION_USER_SERVICIO.S_USER_SERVICIO_ID
                WHERE   
                    s_user_servicio.PER_SERVICIO_ID = '{service}'    
                    AND 
                    s_user_servicio.USER_ID = '{user}'"""
            
            # Ejecutar la consulta
            cursor.execute(query)
            result = cursor.fetchone()   
            
            # Cerrar cursor y conexión
            cursor.close()
            conn.close()

            # Si el resultado es mayor a cero, el usuario es válido
            if result and result[0] > 0:
                user_id = result[0]
                return {'valid': True, 'user_id': user_id}
            else:
                return {'valid': False}
        except Exception as e:
            error_message = str(e)
            log_file_name = datetime.now().strftime('%Y-%m-%d') + '.txt'
            log_file_path = os.path.join('logs', log_file_name)
            with open(log_file_path, 'a') as log_file:
                log_file.write(error_message + '\n' + 'user not valid for user_id ' + user_id)

            print(e)
            return {'valid': False} 