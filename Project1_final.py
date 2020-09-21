import pandas as pd
import warnings

warnings.filterwarnings("ignore")
col_names = ['user_id','item_id','rating','timestamp']
df = pd.read_csv('u.data',sep='\t',names=col_names)

data = pd.read_csv("u.item",sep='\|',header=None)
data = data[[0,1]]
data.columns = ['item_id','movie_name']
df = pd.merge(df,data,on = 'item_id')

ratings = pd.DataFrame(df.groupby('movie_name').mean()['rating'])
ratings['Num of movie'] = pd.DataFrame(df.groupby('movie_name').count()['rating'])
moviemat = df.pivot_table(index='user_id' , columns='movie_name' , values='rating')

def movie_rat(movie,t):
    movie_user_ratings = moviemat[movie]
    similar_movie = moviemat.corrwith(movie_user_ratings)
    corr_movie = pd.DataFrame(similar_movie,columns=['correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings['Num of movie'])
    corr_movie = corr_movie[corr_movie['Num of movie'] > 100]
    print(corr_movie.sort_values(by='correlation',ascending=False).head(n=t))

a = input("Enter movie Name brother will show u movies related to that yyooyyo\n")
b = int(input("Brother how many recomendations should I show U\n"))
movie_rat(a,b)
