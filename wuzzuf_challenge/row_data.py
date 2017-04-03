___author__ = 'Ahmed Hani Ibrahim'


class RowData():
    def __init__(self, i_d, city_name, displayed_job_title,
                 job_category_1, job_category_2, job_category_3,
                 job_industry_1, job_industry_2, job_industry_3,
                 min_salary, max_salary, num_vacancies, career_level,
                 experience_years, post_date, num_views, description,
                 job_requirements):
        self.__i_d = i_d
        self.__city_name = city_name
        self.__displayed_job_title = displayed_job_title
        self.__job_category_1 = job_category_1
        self.__job_category_2 = job_category_2
        self.__job_category_3 = job_category_3
        self.__job_industry_1 = job_industry_1
        self.__job_industry_2 = job_industry_2
        self.__job_industry_3 = job_industry_3
        self.__min_salary = min_salary
        self.__max_salary = max_salary
        self.__num_vacancies = num_vacancies
        self.__career_level = career_level
        self.__experience_years = experience_years
        self.__post_date = post_date
        self.__num_views = num_views
        self.__description = description
        self.__job_requirements = job_requirements

    def get_i_d(self):
        return self.__i_d

    def get_city_name(self):
        return self.__city_name

    def get_displayed_job_title(self):
        return self.__displayed_job_title

    def get_job_category_1(self):
        return self.__job_category_1

    def get_job_category_2(self):
        return self.__job_category_2

    def get_job_category_3(self):
        return self.__job_category_3

    def get_job_industry_1(self):
        return self.__job_industry_1

    def get_job_industry_2(self):
        return self.__job_industry_2

    def get_job_industry_3(self):
        return self.__job_industry_3

    def get_min_salary(self):
        return self.__min_salary

    def get_max_salary(self):
        return self.__max_salary

    def get_num_vacancies(self):
        return self.__num_vacancies

    def get_career_level(self):
        return self.__career_level

    def get_experience_years(self):
        return self.__experience_years

    def get_post_date(self):
        return self.__post_date

    def get_num_views(self):
        return self.__num_views

    def get_description(self):
        return self.__description

    def get_job_requirements(self):
        return self.__job_requirements

