DIRECTORIO_JSON="/mnt/c/Users/tu_usuario/Documentos/datos_usuarios"

NOMBRE_BUCKET="jdjv-so-ueia-2024"

for archivo in "$DIRECTORIO_JSON"/*.json; do
    if [ -f "$archivo" ]; then
        aws s3 cp "$archivo" s3://$NOMBRE_BUCKET/
        if [ $? -eq 0 ]; then
            echo "Archivo $archivo copiado a S3 exitosamente."
            rm "$archivo"  
        else
            echo "Error al copiar $archivo a S3."
        fi
    fi
done
