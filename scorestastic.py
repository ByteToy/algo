import pymysql
import configparser

class ScoreStastic:
    def __init__(self):
        con_f="config.ini"
        conf=configparser.ConfigParser()
        conf.read(con_f,encoding='utf-8')
        sections=conf.sections()
        # print(conf.items('aliyun'))

        # 连接数据库
        self.conn = pymysql.connect(host=conf['aliyun']['host'],
                                    user=conf['aliyun']['user'],
                                    password=conf['aliyun']['password'],
                                    database=conf['aliyun']['database'])
        self.cursor=self.conn.cursor()

    def query_db_version(self):
        self.cursor.execute("select version()")
        data = self.cursor.fetchone()
        print(data)

    def update_score_s_order(self,type):
        drop_tmp_score='DROP TEMPORARY TABLE IF EXISTS tmp_score;'
        self.cursor.execute(drop_tmp_score)
        create_tmp_score='CREATE TEMPORARY table tmp_score as SELECT s.num,s.class,s.name,s.score,(rank() over(order BY s.score DESC)) as s_order FROM s_score s WHERE s.type=%s;'
        self.cursor.execute(create_tmp_score,type)
        update_score_order='UPDATE s_score SET s_order=(SELECT s_order FROM tmp_score WHERE tmp_score.num=s_score.num AND s_score.type=%s) where s_score.type=%s;'
        self.cursor.execute(update_score_order,[type,type])
        self.conn.commit()

    def update_score_f_order(self,type,opt):
        drop_tmp_score = 'DROP TEMPORARY TABLE IF EXISTS tmp_score;'
        self.cursor.execute(drop_tmp_score)
        create_tmp_score = 'CREATE TEMPORARY table tmp_score as SELECT s.num,s.class,s.name,s.score,(rank() over(order BY s.score DESC)) as f_order FROM s_score s WHERE s.type=%s and s.opt=%s;'
        self.cursor.execute(create_tmp_score,[type,opt])
        update_score_order = 'UPDATE s_score SET f_order=(SELECT f_order FROM tmp_score WHERE tmp_score.num=s_score.num AND s_score.type=%s and s_score.opt=%s) where s_score.type=%s and s_score.opt=%s;'
        self.cursor.execute(update_score_order, [type, opt,type,opt])
        self.conn.commit()

    def update_score_order(self):
        type_list=['总分','语文','数学','外语','物理','历史','化学','生物','政治','地理']
        opt_list=['物理','历史']

        for type in type_list:
            self.update_score_s_order(type)

        for type in type_list:
            for opt in opt_list:
                self.update_score_f_order(type,opt)

if __name__=="__main__":
    s_stastic=ScoreStastic()
    s_stastic.query_db_version()
    # s_stastic.update_score_s_order('语文')
    # s_stastic.update_score_f_order('总分','物理')
    # s_stastic.update_score_order()