
stream = 0



vedio_dir = 'DATA/'
classifier_model = 'models/resnet-34_kinetics.onnx'


pose_model = 'models/pose.tflite'
body_dict = {0:'head', 1: 'neck', 2: 'lshoulder', 3:'lelbow',
             4:'lwrist', 5:'rshoulder', 6:'relbow', 7:'rwrist',
             8:'lhip', 9:'lknee', 10:'lankle', 11:'rhip', 12:'rknee', 13:'rankle'}
