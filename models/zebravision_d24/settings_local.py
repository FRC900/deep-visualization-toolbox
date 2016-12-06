# Define critical settings and/or override defaults specified in
# settings.py. Copy this file to settings_local.py in the same
# directory as settings.py and edit. Any settings defined here
# will override those defined in settings.py



# Set this to point to your compiled checkout of caffe
caffevis_caffe_root      = '/home/ubuntu/caffe-viz'

# Load model: caffenet-yos
# Path to caffe deploy prototxt file. Minibatch size should be 1.
caffevis_deploy_prototxt = '/home/ubuntu/2016VisionCode/zebravision/d24/deploy.prototxt'

# Path to network weights to load.
caffevis_network_weights = '/home/ubuntu/2016VisionCode/zebravision/d24/snapshot_iter_1778088.caffemodel'

# Other optional settings; see complete documentation for each in settings.py.
caffevis_labels          = '/home/ubuntu/2016VisionCode/zebravision/d24/labels.txt'

caffevis_label_layers    = ('fc2_d24', 'softmax')
caffevis_prob_layer      = 'softmax'
#caffevis_unit_jpg_dir    = '%DVT_ROOT%/models/caffenet-yos/unit_jpg_vis'
#caffevis_jpgvis_layers   = ['conv1', 'conv2', 'conv3', 'conv4', 'conv5', 'fc6', 'fc7', 'fc8', 'prob']
#caffevis_jpgvis_remap    = {'pool1': 'conv1', 'pool2': 'conv2', 'pool5': 'conv5'}


input_updater_zca_weights = 'models/zebravision_d24/zcaWeights.txt.bz2'
def caffevis_layer_pretty_name_fn(name):
    return name.replace('conv','c').replace('relu','r').replace('pool','p').replace('_d24','')

# Use GPU? Default is True.
caffevis_mode_gpu = False
# Display tweaks.
# Scale all window panes in UI by this factor
#global_scale = 1.0
# Scale all fonts by this factor    
#global_font_size = 1.0
