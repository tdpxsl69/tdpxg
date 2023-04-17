import instaloader
from colorama import Fore, Style
import os
import time
import sys

# Function to get profile information
def get_profile_info(username):
    try:
        # Create an Instaloader instance
        L = instaloader.Instaloader()
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Extract profile information
        full_name = profile.full_name
        follower_count = profile.followers
        following_count = profile.followees
        post_count = profile.mediacount
        is_private = profile.is_private

        # Check if account is private or public
        account_status = "Private" if is_private else "Public"

        # Extract profile picture link
        profile_pic_link = profile.get_profile_pic_url()

        # Extract profile link
        profile_link = f"https://www.instagram.com/{username}/"

        # Extract profile bio
        profile_bio = profile.biography

        # Create file path on desktop
        desktop_path = os.path.expanduser("~/Desktop")
        file_path = os.path.join(desktop_path, f"{username}_info.txt")

        # Write profile information to file
        with open(file_path, "w") as file:
            file.write(f"Account Status: {account_status}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Followers: {follower_count}\n")
            file.write(f"Following: {following_count}\n")
            file.write(f"Posts: {post_count}\n")
            file.write(f"Profile Picture Link: {profile_pic_link}\n")
            file.write(f"Profile Link: {profile_link}\n")
            file.write(f"Profile Bio: {profile_bio}\n")  # Added line to write profile bio

        # Print profile information in CLI in white color
        print(Style.RESET_ALL)
        print(f"Account Status: {account_status}")
        print(f"Username: {username}")
        print(f"Full Name: {full_name}")
        print(f"Followers: {follower_count}")
        print(f"Following: {following_count}")
        print(f"Posts: {post_count}")
        print(f"Profile Picture Link: {profile_pic_link}")
        print(f"Profile Link: {profile_link}")
        print(f"Profile Bio: {profile_bio}")  # Added line to print profile bio

        # Print success message in green color
        print(Fore.GREEN + f"\nProfile information has been saved to {file_path}")
        sys.stdout.flush()  # Flush the stdout buffer to make sure the message is displayed immediately
        time.sleep(2)  # Add a delay of 2 seconds
        sys.exit()  # Exit the program

    except Exception as e:
        print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    # Set welcome text color to green
    print(Fore.GREEN + """.::: .::::::.:::::    .:::::::  .::      .::   .::::   
     .::    .::   .:: .::    .:: .::   .::   .:    .:: 
     .::    .::    .::.::    .::  .:: .::   .::        
     .::    .::    .::.:::::::      .::     .::        
     .::    .::    .::.::         .:: .::   .::   .::::
     .::    .::   .:: .::        .::   .::   .::    .: 
     .::    .:::::    .::       .::      .::  .:::::   
                                                       

    """)
    time.sleep(3)

    print("Welcome to tdpxg - Instagram Profile Analyzer")
    print("Made by tdpxsl69")
    time.sleep(2)
    print(Style.RESET_ALL)
    while True:
        print("\nPlease choose an option:")
        print("1. Get Instagram Profile Information")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            username = input("Enter Instagram username: ")
            get_profile_info(username)
        elif choice == "2":
            print("Exiting...")
            time.sleep(2)  # Add a delay of 2 seconds before exiting
            break
        else:
            print("Invalid choice. Please choose again.")
