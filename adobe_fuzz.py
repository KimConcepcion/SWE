from fuzzing.fuzzer import FuzzExecutor

file_list = ["./phd2004.pdf", "./Omregningstabel.pdf", "./good_concepts.pdf"]
apps_under_test = ["/Program Files (x86)/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe"]

number_of_runs = 13

def test():
	print("Starting test")
	fuzz_executor = FuzzExecutor(apps_under_test, file_list)
	fuzz_executor.run_test(number_of_runs)
	return fuzz_executor.stats

def main():
	stats = test()
	print(stats)

if __name__ == '__main__':
	main()


