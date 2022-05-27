import torchvision.models as models
import torch
import torch.nn as nn
import numpy as np

class MyCNN(nn.Module):
    """Builds a CNN using a pre-trained neural network replacing the final layers for a custom image task
    
    Args:
        model_base: Model choice for pre-trained network
        input_shape: 3D shape of input tensor
    """
    def __init__(self, model_base='resnet101', input_shape=(3,224,224)):
        super().__init__()
        self.pretrained = initialise_model(model_base)                         # load pre-trained model
        dim = get_final_dimension(self.pretrained, input_shape)
        self.my_new_layers = nn.Sequential(nn.Flatten(),
                                            nn.Linear(dim, 512),               # add fully connected layer
                                            nn.Linear(512, 256),               # add fully connected layer
                                            nn.Linear(256,1))                  # final output is 1 for regression task

    def forward(self, x):
        x = x.float()
        x = self.pretrained(x)
        x = self.my_new_layers(x)
        return x

    def count_params(self):
        pytorch_total_params = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return pytorch_total_params

# where should these function be?
def initialise_model(model_base):
    """ Function to initiliase pre-trained model and remove final layers
    """
    method_to_call = getattr(models, model_base)
    model = method_to_call(pretrained=True)                                     # load pre-trained model
    model = nn.Sequential(*(list(model.children())[:-2]))                       # remove final layers
    return model

def get_final_dimension(model, input_shape):
    """ Calculates output of pre-trained model given image input_shape
    """
    x = torch.randn( (1,) + input_shape)        
    out = model(x)
    return np.prod(out.shape)