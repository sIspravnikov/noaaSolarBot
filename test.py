def main():
    sources = {
      'lascoC2': {
         'extension': 'jpg', 
         'url': 'https://services.swpc.noaa.gov/images/animations/lasco-c2/',
      },
      'lascoC3': {
         'extension': 'jpg', 
         'url': 'https://services.swpc.noaa.gov/images/animations/lasco-c3/',
      }
    }
    
    for key,value in sources.items():
        print(key, value['extension'])

if __name__ == '__main__':
   main()