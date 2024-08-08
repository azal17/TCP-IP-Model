import matplotlib.pyplot as plt

def plot(x, y):
    plt.step(x, y, where='mid')
    plt.xlabel('Bit Index')
    plt.ylabel('Bit Value')
    plt.title('Rectangular Plot for AMI Line Encoding')
    plt.yticks([-1, 0, 1])
    plt.ylim(-1.5, 1.5)
    plt.show()

def AMI():
    bitstream = input("Enter the bitstream: ")
    input_array = range(len(bitstream))
    output_array = []
    count = 0
    for char in bitstream:
        if char == '0':
            output_array.append(0)
        elif char == '1':
            if count % 2 == 0:
                output_array.append(1)
            else:
                output_array.append(-1)
            count += 1
    plot(input_array, output_array)

AMI()
