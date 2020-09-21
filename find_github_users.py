from github import Github

ACCESS_TOKEN = 'YOUR GITHUB TOKEN'

g = Github(ACCESS_TOKEN)


def search_github():
    query = ' '.join(keywords) + {True: '',False: ' language:'}[languages == ['']] +'+language:'.join(languages) + {True: '',False: ' location:' + country }[country == '']
    print('The query is ->' + query)
    result = g.search_users(query , 'followers', 'desc')
    print(f'Found {result.totalCount} repo(s)')
    
    f = open(filename,'w')
    f.write('name, url, hireable, number of followers, blog url, email, updated_at \n')
    for repo in result:
        print(f'{repo.name}, https://www.github.com/{repo.login}, {repo.hireable}, {repo.followers} followers')
        f.write(f"{repo.name}, https://www.github.com/{repo.login}, {repo.hireable}, {repo.followers}, {repo.blog}, {repo.email}, {repo.updated_at} \n")
    f.close()


if __name__ == '__main__':
    filename = input('Enter a filename (e.g estonia_webrtc_nov.csv):')
    country = input('Enter a country: [leave blank for world]')
    keywords = input('Enter keyword(s)[e.g webrtc]: ')
    languages = input('Enter langauge(s)[e.g C++, javascript]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    languages = [language.strip() for language in languages.split(',')]
    search_github()
