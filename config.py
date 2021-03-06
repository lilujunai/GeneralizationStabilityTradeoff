run_cfgs = {
    
    # Figure 2 configurations for VGG 
    # Some of these are *not* plotted in Fig 2,
    # but we use all of these configurations in Figure 6.
    # We also reuse the F2_VGG_0 configuration as a baseline when needed
    'F2_VGG_0': {'lr_schedule':[150, 300], 
            'gen_matrices': True},
    'F2_VGG_1': {'lr_schedule':[150, 300], 
            'gen_matrices': True, 
            'pre_prune_acc': True,
            'prune_frac' : [.3,.3,.3,.9],                       
            'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
            'retrain_period':4, 
            'prune_random':False, 
            'target_large':False},
    'F2_VGG_2': {'lr_schedule':[150, 300], 
            'gen_matrices': True, 
            'pre_prune_acc': True,
            'prune_frac' : [.3,.3,.3,.9],                       
            'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
            'retrain_period':40, 
            'prune_random':False, 
            'target_large':False},
    'F2_VGG_3': {'lr_schedule':[150, 300], 
            'gen_matrices': True, 
            'pre_prune_acc': True,
            'prune_frac' : [.3,.3,.3,.9],                       
            'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
            'retrain_period':40, 
            'prune_random':True},
    'F2_VGG_4': {'lr_schedule':[150, 300], 
            'gen_matrices': True, 
            'pre_prune_acc': True,
            'prune_frac' : [.3,.3,.3,.9],                       
            'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
            'retrain_period':40, 
            'prune_random':False, 
            'target_large':True},
    'F2_VGG_5': {'lr_schedule':[150, 300], 
            'gen_matrices': True, 
            'pre_prune_acc': True,
            'prune_frac' : [.3,.3,.3,.9],                       
            'prune_start_epoch': [0,0,0,0], 'prune_end_epoch': [0,0,0,0],
            'retrain_period':4, 
            'prune_random':False, 
            'target_large':False, 
            'scratch_prune': True},
    
    # Figure 2 configurations, ResNet18 
    'F2_RN_0': {'lr_schedule':[150, 300]},
    'F2_RN_1': {'lr_schedule':[150, 300],
                 'pre_prune_acc': True, 
                 'prune_frac' : [.25,.4,.25,.95], 
                 'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                 'retrain_period':4,
                 'target_large' : False,
                 'scoring': 'activations'},
    'F2_RN_2': { 'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.4,.25,.95],
                'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'target_large' : False,
                'scoring': 'activations'},
    'F2_RN_3': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.4,.25,.95], 
                'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'scoring': 'activations'},
       
    
    # Figure 5 configurations 
    'F5_0' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'Prune_L'},
    'F5_1' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_0_zeroing'},
    'F5_2' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_129_zeroing'},
    'F5_3' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_1500_zeroing'},
    'F5_4' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_0_gaussian'},
    'F5_5' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_129_gaussian'},
    'F5_6' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'iter_1500_gaussian'},
    
    
    # Figure B2, VGG
    'FB2_VGG_1': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True,
                'prune_frac' : [.3,.3,.3,.9],                       
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
                'retrain_period':4, 
                'target_large':False,
                'scoring': 'EBN'},
    'FB2_VGG_2': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True,
                'prune_frac' : [.3,.3,.3,.9],                       
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
                'retrain_period':40, 
                'target_large':False,
                'scoring': 'EBN'},
    'FB2_VGG_3': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True,
                'prune_frac' : [.3,.3,.3,.9],                       
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275], 
                'retrain_period':40,
                'scoring': 'EBN'},
    
    # Figure B2, ResNet18
    'FB2_RN_1': {'lr_schedule':[150, 300],
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.4,.25,.95],                      
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':4,
                'target_large' : False,
                'scoring': 'EBN_alt'},
    'FB2_RN_2': { 'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.4,.25,.95],                      
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'target_large' : False,
                'scoring': 'EBN_alt'},
    'FB2_RN_3': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.4,.25,.95],                      
                'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'scoring': 'EBN_alt'},
    
    
    # Table C.1 configurations
    'TC1_1': {'lr_schedule':[150, 300],
                 'pre_prune_acc': True, 
                 'prune_frac' : [.25,.8,.25,.95], 
                 'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                 'retrain_period':4,
                 'target_large' : False,
                 'scoring': 'activations'},
    'TC1_2': { 'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.8,.25,.95],
                'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'target_large' : False,
                'scoring': 'activations'},
    'TC1_3': {'lr_schedule':[150, 300], 
                'pre_prune_acc': True, 
                'prune_frac' : [.25,.8,.25,.95], 
                'prune_start_epoch': [7,8,9,10], 'prune_end_epoch': [150,150,170,275], 
                'retrain_period':40,
                'scoring': 'activations'},
       
    
    # Figure C3 configurations
    'FC3_0': {'lr_schedule':[83, 125],
               'weight_decay': 0.0001,
               'prune_frac' : [.1]*16,
               'scoring' : 'L1',
               'prune_start_epoch': [24]*16,
               'prune_end_epoch': [100]*16,
               'pre_prune_acc': True,
               'retrain_period': 1,
               'target_large' : False},
    'FC3_1':  {'lr_schedule':[83, 125],
               'weight_decay': 0.0001,
               'prune_frac' : [.06]*16,
               'scoring' : 'L1',
               'prune_start_epoch': [24]*16,
               'prune_end_epoch': [100]*16,
               'pre_prune_acc': True,
               'retrain_period': 1,
               'target_large' : False},
    'FC3_2': {'lr_schedule':[83, 125],
                 'weight_decay': 0.0001},

    
    
    # Figure D2 configurations
    'FD2_0' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'cumu_129_zeroing_restore'},
    'FD2_1' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'cumu_750_zeroing_restore'},
    'FD2_2' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'cumu_1500_zeroing_restore'},
    'FD2_3' : {'lr_schedule':[150, 300],
             'pre_prune_acc': True, 
             'prune_frac' : [.3,.3,.3,.9],  
             'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
             'retrain_period':40,
             'noise': 'cumu_3000_zeroing_restore'},
    
    
    # Table F.1 configurations
    'TF1_0' : {'lr_schedule':[2000]},
    'TF1_1' : {'lr_schedule':[2000],
               'pre_prune_acc': True,
               'prune_frac' : [0, 0, 0, .7], 
               'scoring' : 'L1',
               'prune_start_epoch': [0, 0, 0, 2500], 'prune_end_epoch': [0, 0, 0, 3500],
               'retrain_period': 750},
    'TF1_2' : {'lr_schedule':[2000],
               'pre_prune_acc': True,
               'prune_frac' : [0, 0, 0, .7], 
               'scoring' : 'L1',
               'prune_start_epoch': [0, 0, 0, 2500], 'prune_end_epoch': [0, 0, 0, 3500],
               'retrain_period': 750,
               'target_large': False},
    'TF1_3': {'lr_schedule':[2000], 
              'prune_frac' : [0, 0, 0, .7],
              'prune_start_epoch': [0, 0, 0, 0], 'prune_end_epoch': [0, 0, 0, 0], 
              'scratch_prune': True}
    
    
    
    
    }
    

# Figure 3 configurations
for retrain in [4, 20, 40, 60, 100, 200, 300]:
    run_cfgs['F3_S_'+str(retrain)] =  {'lr_schedule':[150, 300],
                    'pre_prune_acc': True, 
                    'prune_frac' : [.3,.3,.3,.9],
                    'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
                    'retrain_period':retrain,
                    'target_large' : False}
    run_cfgs['F3_R_'+str(retrain)] =  {'lr_schedule':[150, 300],
                    'pre_prune_acc': True, 
                    'prune_frac' : [.3,.3,.3,.9],
                    'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
                    'retrain_period':retrain,
                    'prune_random' : True}
    run_cfgs['F3_L_'+str(retrain)] = {'lr_schedule':[150, 300],
                    'pre_prune_acc': True, 
                    'prune_frac' : [.3,.3,.3,.9],
                    'prune_start_epoch': [3,4,5,6], 'prune_end_epoch': [150,150,150,275],
                    'retrain_period':retrain}


# Figure 4 configurations
for resnet in ['18', '20', '56']:
    run_cfgs['F4_'+resnet+'_0'] = {'lr_schedule':[83, 125],
       'weight_decay': 0.0001,
       'prune_frac' : [.1]*(int(resnet)-2),
       'scoring' : 'L1',
       'prune_start_epoch': [40]*(int(resnet)-2),
       'prune_end_epoch': [100]*(int(resnet)-2),
       'pre_prune_acc': True, 
       'retrain_period': 30,
       'target_large' : False}
    run_cfgs['F4_'+resnet+'_1'] = {'lr_schedule':[83, 125],
       'weight_decay': 0.0001,
       'prune_frac' : [.1]*(int(resnet)-2),
       'scoring' : 'L1',
       'prune_start_epoch': [40]*(int(resnet)-2),
       'prune_end_epoch': [100]*(int(resnet)-2),
       'pre_prune_acc': True, 
       'retrain_period': 60,
       'target_large' : False}
