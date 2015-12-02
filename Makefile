run_all_in_parallel:
	make -j iPhone_6 

iPhone_6:
	deviceName="iPhone 6 Device" behave-parallel/bin/behave --processes 12 --parallel-element scenario

