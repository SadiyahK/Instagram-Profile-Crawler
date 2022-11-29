from instagrapi import Client

api = Client()
USERNAME = ""
PASSWORD = ""


def get_user_info():
    api.login(USERNAME, PASSWORD)
    user_id = api.user_id_from_username(USERNAME)

    # get user's followers list
    user_followers = api.user_followers(user_id).values()
    # extract only usernames from UserShort objects
    followers_lst = list((obj.username for obj in user_followers))
    write_to_file("followers", followers_lst)

    # get user's following list
    user_following = api.user_following(user_id).values()
    # extract only usernames from UserShort objects
    following_lst = list((obj.username for obj in user_following))
    write_to_file("following", following_lst)

    # computational insights
    not_following_user = set(following_lst) - set(followers_lst)
    write_to_file("not_following_user", not_following_user)
    user_not_following = set(followers_lst) - set(following_lst)
    write_to_file("user_not_following", user_not_following)


def write_to_file(filename, input_lst):
    with open(f'{filename}.txt', 'w') as f:
        for i in input_lst:
            f.write(f"{i}\n")


if __name__ == '__main__':
    USERNAME = input("Input username:")
    PASSWORD = input("Input password:")
    get_user_info()

