class CakeFactory:
    def createWeddingCake():
        return WeddingCake()

    def createBirthDayCake():
        return BirthdayCake()
    
    def createInformalCake():
        return InformalCake()
    
class ChocolateCakeFactory(CakeFactory):
    def __init__(self):
        super().__init__()

class PineappleCakeFactory(CakeFactory):
    def __init__(self):
        super().__init__()

class CornCakeFactory(CakeFactory):
    def __init__(self):
        super().__init__()

class WeddingCake:
    def writeCongrats(self):
        print('Congrats!')

class BirthdayCake:
    def gift(self):
        print('Take my gift.')

class InformalCake:
    def enjoy(self):
        print("Let's enjoy!")

class ChocolateWeddingCake(WeddingCake):
    def __init__(self):
        super().__init__()

class ChocolateBirthdayCake(BirthdayCake):
    def __init__(self):
        super().__init__()

class ChocolateInformalCake(InformalCake):
    def __init__(self):
        super().__init__()

class PineappleWeddingCake(WeddingCake):
    def __init__(self):
        super().__init__()

class PineappleBirthdayCake(BirthdayCake):
    def __init__(self):
        super().__init__()

class PineappleInformalCake(InformalCake):
    def __init__(self):
        super().__init__()

class CornWeddingCake(WeddingCake):
    def __init__(self):
        super().__init__()

class CornBirthdayCake(BirthdayCake):
    def __init__(self):
        super().__init__()

class CornInformalCake(InformalCake):
    def __init__(self):
        super().__init__()

cake = ChocolateCakeFactory.createWeddingCake()
cake.writeCongrats()