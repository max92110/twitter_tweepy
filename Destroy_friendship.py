import tweepy


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }
  api = get_api(cfg)
  
#Твитнуть список элементов папки
  #tweet = input("Введите сообщение:")
  
  #print(tweet)
  #status = api.update_status(status=tweet) 
  
#Получить кол-во подписчиков
  #status = api.followers_count
  #userlist = api.me().followers
  for user in tweepy.Cursor(api.friends).items():
    # Удалить все подписки кроме:
    if user.screen_name != '':
      api.destroy_friendship(user.screen_name)
  
  
    

if __name__ == "__main__":
  main()
