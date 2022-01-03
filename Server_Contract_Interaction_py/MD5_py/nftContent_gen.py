import hashlib


### func: calculate the `nftContent` when creating a new NFT
### input: 
###     fileContent : str, string read from the model file
### output:
###     str, MD5 hash value of the model file
def getNftContent(fileContent):
    result = hashlib.md5(fileContent.encode())
    return result.hexdigest()


#####################################################
# 使用样例
def demo_getNftContent():
    filePath = "MYFILE.json"
    with open(filePath) as fileHandler:
        # rend file content
        fileContent = fileHandler.read()
        # get hash result
        md5Result = getNftContent(fileContent)

        print(fileContent)
        print(md5Result)
        print(type(md5Result))


demo_getNftContent()
