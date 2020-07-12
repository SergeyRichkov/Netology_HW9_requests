class YaUploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def upload(self):
        import requests
        import os
        
        file_list = os.listdir(self.file_path)
        
        len_file_list = len(file_list )
        sum_response2 = ''
        for file_name in file_list:        
            param = {'path': f'{file_name}', 'overwrite' : True }
            header = {'Authorization':'',}
            response = requests.get(
            'https://cloud-api.yandex.net:443/v1/disk/resources/upload',
            params=param,
            headers=header
            )
            if str(response)!= '<Response [200]>':
                print('Ошибка загрузки:', response.json()['message'])
                return
            
            href = response.json()['href']

            with open(self.file_path + '\\' +  file_name, 'rb') as f:
                file_ = f.read()

                response2 = str(requests.put(href, data = file_))
                sum_response2 += response2
                print(sum_response2)
        if sum_response2 == len_file_list * '<Response [201]>':
            print(f'{len_file_list} файлов успешно загружены на диск')
        else:
            print('Ошибка загрузки')
        return 


if __name__ == '__main__':
    uploader = YaUploader('C:\python_example')
    result = uploader.upload()



