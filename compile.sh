nvcc -gencode arch=compute_20,code=sm_20  bfs.cu -g -G -o bfs.out -I/usr/local/cuda/include -L/usr/local/cuda/lib64
#nvcc -arch=sm_20  bfs.cu -g -G -o bfs.out -I/usr/local/cuda/include -L/usr/local/cuda/lib64

#Add to end of log file
#This is for generateDynamic.py
#INFO [Launch of CUDA Kernel 0 (matrixMulCUDA<32><<<(4,6,1),(32,32,1)>>>) on Device 0]
