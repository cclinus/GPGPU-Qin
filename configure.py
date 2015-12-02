#configuration for the kernel 
startline = "matrixMul.cu:46"
benchmark = "matrix"
kernel = "matrixMulCUDA"
multiple_kernel = 0
kernel_number = ['86','87']
#configuration for the profile
model = "telsa2070"  # GPU model for multiple GPUs
profile_file = benchmark+"_"+kernel+"_"+model+"_"+"profiler.log"
#profile_file = "sadprofiler.log.kernel2"

#configuration for the injection
startingpc = 8689144 #8502888  # the first pc from the profile
sm =14  # number of StreamingMultiprocessor

instruction_counter = 300 # better to keep it like this
instruction_random = 0  # better to keep it like this

#configuration for launching the benchmark
parameter = ""
#parameter = " -i ~/parboil/datasets/sad/default/input/reference.bin,/home/bo/parboil/datasets/sad/default/input/frame.bin -o output"
binary_path = "/home/gpli/NVIDIA_CUDA-6.0_Samples/0_Simple/matrixMul/matrixMul"

#correctness check
outputfile = "/home/bo/topK_thrust/topK/output/beamOutput.txt"
comparestring = "/home/bo/parboil/benchmarks/sad/tools/compare-output /home/bo/parboil/datasets/sad/default/output/out.bin ./output"
checkstring = "PASSED"
