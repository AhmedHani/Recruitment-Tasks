___author__ = 'Ahmed Hani Ibrahim'


import pandas as pd
from bs4 import BeautifulSoup
from row_data import RowData


class DataReader(object):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__wuzzuf_data = []

    def read_data(self):
        df_wuzzuf_data = pd.read_csv(self.__file_path)
        size = len(df_wuzzuf_data['id'])

        for i in range(1, size):
            i_d = df_wuzzuf_data['id'][i]
            city_name = df_wuzzuf_data['city_name'][i]
            displayed_job_title = df_wuzzuf_data['displayed_job_title'][i]
            job_category_1 = df_wuzzuf_data['job_category_1'][i]
            job_category_2 = df_wuzzuf_data['job_category_2'][i]
            job_category_3 = df_wuzzuf_data['job_category_3'][i]
            job_industry_1 = df_wuzzuf_data['job_industry_1'][i]
            job_industry_2 = df_wuzzuf_data['job_industry_2'][i]
            job_industry_3 = df_wuzzuf_data['job_industry_3'][i]
            min_salary = df_wuzzuf_data['salary_min'][i]
            max_salary = df_wuzzuf_data['salary_max'][i]
            num_vacancies = df_wuzzuf_data['num_vacancies'][i]
            career_level = df_wuzzuf_data['career_level'][i]
            experience_years = df_wuzzuf_data['experience_years'][i]
            post_date = df_wuzzuf_data['post_date'][i]
            num_views = df_wuzzuf_data['views'][i]
            description = self.__clean_text(df_wuzzuf_data['description'][i])
            job_requirements = self.__clean_text(df_wuzzuf_data['job_requirements'][i])

            obj = RowData(i_d, city_name, displayed_job_title,
                                              job_category_1, job_category_2, job_category_3,
                                              job_industry_1, job_industry_2, job_industry_3,
                                              min_salary, max_salary, num_vacancies,
                                              career_level, experience_years, post_date,
                                              num_views, description, job_requirements)

            self.__wuzzuf_data.append(obj)

        return self.__wuzzuf_data

    def __clean_text(self, text):
        if str(text) == 'nan':
            return ""

        soup = BeautifulSoup(text, 'html.parser')
        clean_text = soup.get_text().strip()

        return clean_text






