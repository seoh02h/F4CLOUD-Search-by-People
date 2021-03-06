import boto3

def list_faces_in_collection(collectionId):
    collection_id = collectionId
    max_results = 100
    faces_count = 0
    tokens = True

    client = boto3.client('rekognition')
    response = client.list_faces(CollectionId=collection_id,
                                 MaxResults=max_results)

    print('Faces in collection ' + collection_id)

    while tokens:
        faces = response['Faces']

        for face in faces:
            print(face)
            faces_count += 1
        if 'NextToken' in response:
            nextToken = response['NextToken']
            response = client.list_faces(CollectionId=collection_id,
                                         NextToken=nextToken, MaxResults=max_fesults)
        else:
            tokens = False
    return faces_count


def main():
    #collection_id = '<collection_id>'

    faces_count = list_faces_in_collection(collection_id)
    print("faces count: " + str(faces_count))


if __name__ == "__main__":
    main()