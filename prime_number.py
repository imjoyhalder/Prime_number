try: 
    class test_prime:
        def __init__(self,n):
            self.number = n
        def prime(self):
            if self.number == 1:
                return " 1 is not Prime number"
            elif self.number == 2 :
                return "2 is Prime number"
            else:
                for i in range(2,self.number):
                    if self.number%i == 0:
                        return f"{self.number} is not prime number"
                return f"{self.number} is prime number" 
           
    while True: 
        try:        
            object = test_prime(int(input("Input Number: ")))
            print(object.prime())
            break
        except ValueError as v:
            print("Invalid Value ")
            continue
except Exception as e:
    print(e)
finally:
    print("Me")