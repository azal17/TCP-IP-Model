class Switch:
    def __init__(self, device):
        self.device = device
        self.mapping = {}

    def get_switch_details(self):
        for i in range(self.device.n):
            sender, receiver = input("Enter sender and receiver: ").split()
            if i == 0:
                for j in range(self.device.N):
                    self.mapping[self.device.get_products()[j].name] = self.device.get_products()[j].mac_address
                print("Message from", sender, "broadcasted to all devices")
            else:
                print("Message received by", receiver, "at address", self.mapping.get(receiver, "Unknown"))


class Device:
    def __init__(self):
        self.name = None
        self.mac_address = None
        self.N = None
        self.n = None

    def get_details(self):
        self.N = int(input("Enter the number of devices: "))
        self.n = int(input("Enter the number of queries: "))

    def get_products(self):
        devices = []
        for i in range(self.N):
            device = Device()
            device.name = chr(65 + i)  
            device.mac_address = 100 * (i + 1)  
            devices.append(device)
        return devices

    def domains(self):
        print(f"The number of collision domains is {self.N}")
        print(f"The number of broadcast domains is 1")


def main():
    d = Device()
    d.get_details()
    products = d.get_products()
    d.domains()
    s = Switch(d)
    s.get_switch_details()


if __name__ == "__main__":
    main()
