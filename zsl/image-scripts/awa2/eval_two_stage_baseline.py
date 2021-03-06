import os

os.system('''CUDA_VISIBLE_DEVICES=3 OMP_NUM_THREADS=8 python train_tfvaegan_inductive.py --gammaD 10 \
--gammaG 10 --gzsl --encoded_noise --manualSeed 9182 --preprocessing --cuda --image_embedding res101 \
--class_embedding att --nepoch 200 --syn_num 400 --ngh 4096 --ndh 4096 --lambda1 10 --critic_iter 5 \
--nclass_all 50 --dataroot /data2/xxx/Dataset/zsl/ps2/xlsa17/data --dataset AWA2 \
--batch_size 64 --nz 85 --latent_size 85 --attSize 85 --resSize 2048 --encoder_use_y \
--lr 0.00001 --classifier_lr 0.001 --recons_weight 0.1 --freeze_dec --save_interval 40 \
--feed_lr 0.0001 --dec_lr 0.0001 --feedback_loop 2 --a1 0.01 --a2 0.01 --val_interval 5 --clf_epoch 2 \
--eval --continue_from 120 \
--use_mask best_masks/awa2/baseline \
--eval --two_stage \
--u_num 1800 --u_epoch 2 --u_batch_size 1800''')