import boto3

s3 = boto3.client('s3')

bucket_name = 'devops-rafa-inventario'

file_name = 'README.md'

s3.upload_file(file_name, bucket_name, file_name)

print(f'Archivo {file_name} subido correctamente a {bucket_name}')
