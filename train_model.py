from darkflow.net.build import TFNet

option={
	'model' : 'cfg/tiny-yolo-id-card.cfg',
	'load' :'bin/tiny-yolo-voc.weights',
	'batch' : 8,
	'epoch' : 1,
	'gpu'	: 1.0,
	'train' : True,
	'annotation' : 'id-card-model/annotation',
	'dataset' : 'id-card-model/image'
}

tfnet = TFNet(option)
tfnet.train()