import matplotlib.pyplot as plt


with open('test_results', 'r') as results:
    tests = results.read().splitlines()
    times_naive = [float(x.split()[0]) for x in tests]
    times_cache_oblivious = [float(x.split()[1]) for x in tests]

input_data_sizes = list(range(50, 750, 50)) + list(range(1000, 9000, 1000))
plt.title('Comparison of naive and cache-oblivious matrix transposing algorithms')
plt.ylabel('time in ms')
plt.xlabel('matrix width and height')
plt.plot(input_data_sizes, times_cache_oblivious, 'g', input_data_sizes, times_naive, 'r')
plt.savefig('graphic.png')