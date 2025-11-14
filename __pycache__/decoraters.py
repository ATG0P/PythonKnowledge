def home(fx):
    def mfx():
        print("Welcome to our Home")
        fx()
        print("thank you")
    return mfx
@home
def vector():
    print("This way pls")
vector()