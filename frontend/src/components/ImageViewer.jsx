import React, { useState, useEffect } from "react";
import axios from "axios";

const ImageViewer = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    axios
      .get("http://10.101.4.17:9001/api/getimages/")
      .then((response) => {
        console.log(response.data);
        setImages(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener las imágenes:", error);
      });
  }, []);

  const algo = {
    readyState: 4,
    responseText: '{"error":"User validation failed.","success":"false"}',
    responseJSON: { error: "User validation failed.", success: "false" },
    status: 400,
    statusText: "Bad Request",
  };  

  return (
    <div className="container mt-5">
      <h2 className="text-center">Visor de Imágenes</h2>
      <hr />
      <div className="row mt-2">
        {images.map((image, index) => (
          <div key={index} className="col-md-4 mb-4">
            <div className="card card-body shadow-lg rounded">
              <div className="card-image text-center">
                <img
                  key={index}
                  src={`data:image/png;base64,${image.image_base64}`} // Cambia "image_base64" por la propiedad que contiene el string base64 en tu objeto JSON
                  alt={image.name}
                  className="img-fluid"
                />
              </div>
              <div className="card-text text-center mt-2">
                <h6>image name: {image.name}</h6>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ImageViewer;
