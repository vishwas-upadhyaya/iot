# import boto3
#
# import environ
#
# env = environ.Env()
# # reading .env file
# environ.Env.read_env()
#
# # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# # SECRET_KEY = env("SECRET_KEY")
# aws_access_key_id = env("AWS_ACCESS_KEY_ID")
# aws_secret_access_key = env("AWS_SECRET_ACCESS_KEY")
# region_name = env("AWS_REGION")
#
#
# print(region_name)
#
# client = boto3.client("textract", region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
#
#
# def convert(path):
#     print("hello")
#     with open(path, "rb") as image_file:
#         response = client.detect_document_text(Document={"Bytes": image_file.read()})
#     res = ""
#     for item in response["Blocks"]:
#         if item["BlockType"] == "LINE":
#             # print(item["Text"])
#             res = item["Text"]
#         # print(detection[1])  # detection[1] contains the recognized text
#     print(res)
#     res = get_text(res)
#     path1 = path.split("\\")
#     path1 = path1[len(path1)-1].split(".")[0]+".mp3"
#
#     return texttospeech(res,path1)