from github import Github

ACCESS_TOKEN = 'YOUR GITHUB TOKEN'

g = Github(ACCESS_TOKEN)


def search_github(keywords):
    query = 'language:'+' language:'.join(keywords) + ' location:' + country 
    print('The query is ->' + query)
    result = g.search_users(query , 'followers', 'desc')
    print(f'Found {result.totalCount} repo(s)')
    
    f = open(filename,'w')
    f.write('name, url, hireable, number of followers, location, blog url, email, updated_at \n')
    for repo in result:
        print(f'{repo.name}, https://www.github.com/{repo.login}, {repo.hireable}, {repo.followers} followers')
        f.write(f"{repo.name}, https://www.github.com/{repo.login}, {repo.hireable}, {repo.followers}, {repo.location.replace(',', ' ')}, {repo.blog}, {repo.email}, {repo.updated_at} \n")
    f.close()


if __name__ == '__main__':
    filename = input('Enter a filename (e.g estonia_webrtc_nov.csv):')
    country = input('Enter a country:')
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    print(keywords)
    search_github(keywords)

