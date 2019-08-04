from darkflow.net.build import TFNet

options = {
	'model' : 'cfg/tiny-yolo-id-card.cfg',
	'load' : -1,
	'batch' : 8,
	'epoch' : 1,
	'gpu'	: 1.0,
	'train' : True,
	'annotation' : 'id-card-model/annotation',
	'dataset' : 'id-card-model/image'
}

tfnet = TFNet(options)
tfnet.load_from_ckpt()	#load latest checkpointing loads...
tfnet.train()