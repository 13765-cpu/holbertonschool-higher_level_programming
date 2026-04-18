import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        # Lazımi sütunları seçib siyahı düzəldirik
        data_to_save = []
        for post in posts:
            data_to_save.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
            
        # CSV-yə yazma hissəsi
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
