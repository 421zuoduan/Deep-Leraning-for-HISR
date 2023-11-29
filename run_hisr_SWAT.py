from UDL.hisr.common.main_hisr import main
from UDL.Basis.auxiliary import set_random_seed
# from UDL.hisr.HISR.SWAT_baseline.option_hisr_SWAT import cfg as args
# from UDL.hisr.HISR.SWAT_baseline.model_SWAT import build
# from UDL.hisr.HISR.SWAT_baseline_noshift.option_hisr_SWAT import cfg as args
# from UDL.hisr.HISR.SWAT_baseline_noshift.model_SWAT import build
# from UDL.hisr.HISR.SWATv1.option_hisr_SWAT import cfg as args
# from UDL.hisr.HISR.SWATv1.model_SWAT import build
# from UDL.hisr.HISR.SWATv2.option_hisr_SWAT import cfg as args
# from UDL.hisr.HISR.SWATv2.model_SWAT import build
from UDL.hisr.HISR.SWATv3.option_hisr_SWAT import cfg as args
from UDL.hisr.HISR.SWATv3.model_SWAT import build



import os
if __name__ == '__main__':
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  # see issue #152
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    # cfg = Config.fromfile("../pansharpening/DCFNet/option_DCFNet.py")
    set_random_seed(args.seed)
    # print(cfg.builder)
    # print(model_DFTL_v1)
    # log_string(args)
    args.builder = build
    main(args)
#
# if __name__ == '__main__':
#     import glob
#     import shutil
#     fdir = "./my_model_results/Rain200L/"
#     flist = glob.glob(fdir + "*.png")
#     for file in flist:
#         print(file)
#         # shutil.move(file, file.split('.')[0][:-3]+'.png')