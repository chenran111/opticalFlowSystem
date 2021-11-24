# !/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from flask import Flask, jsonify, request
import datetime


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示


@app.route("/submit", methods=['POST'])
def video_submit():
    id = request.json.get("id").strip()  # 主键（业务ID）
    devID = request.json.get("devID").strip()  # 视频设备ID
    algID = request.json.get("algID").strip()  # 智能算法ID
    staTime = request.json.get("staTime", datetime.datetime.now().strftime('%T')).strip()  # 开始时间，当天时间，默认为当前时间
    endTime = request.json.get("endTime", "24:00:00").strip()  # 结束时间，当天时间，默认为24:00:00
    repPeriod = request.json.get("repPeriod", 1)  # 重复周期，正整数，默认为1，表示一天
    repNumber = request.json.get("endTime", 1)  # 重复次数，非正数时表示永久重复，默认为1
    priority = request.json.get("priority", 0)  # 优先级，默认为0
    comments = request.json.get("comments", "").strip()  # 备注

    tmp = []
    with open('business_data.txt', 'r') as f:
        for line in f:
            tmp.append(json.loads(line))

    if id and devID and algID:
        for i in range(len(tmp)):
            if tmp[i]["id"] == id:
                return jsonify({"code": "2006", "msg": "该主键已经存在，请检查！！！"})
            else:
                staTime_list = staTime.split(':')
                staTime_data = [int(x) for x in staTime_list]
                SH = staTime_data[0]
                SM = staTime_data[1]
                SS = staTime_data[2]
                endTime_list = endTime.split(':')
                endTime_data = [int(x) for x in endTime_list]
                EH = endTime_data[0]
                EM = endTime_data[1]
                ES = endTime_data[2]
                if not ((SH >= 0) and (SH < 24) and (SM >= 0) and (SM < 60) and (SS >= 0) and (SS < 60)):
                    return jsonify({"code": 2002, "msg": "开始时间输入格式不正确！！！"})
                elif not ((EH >= 0) and (EH < 24) and (EM >= 0) and (EM < 60) and (ES >= 0) and (
                        ES < 60) and endTime != "24:00:00"):
                    return jsonify({"code": 2003, "msg": "结束时间输入格式不正确！！！"})
                elif staTime >= endTime:
                    return jsonify({"code": 2004, "msg": "开始时间早于结束时间，请检查！！！"})
                elif priority < 0 or priority > 9:
                    return jsonify({"code": 2005, "msg": "优先级最低为0，最高为9，输入不正确，请检查！！！"})
                else:
                    s = {"id": id, "devID": devID, "algID": algID, "staTime": staTime, "endTime": endTime,
                         "repPeriod": repPeriod, "repNumber": repNumber, "priority": priority, "comments": comments}
                    aa = json.dumps(s, ensure_ascii=False)
                    with open(r"business_data.txt", "a") as f:
                        f.write(aa + '\n')
                    return jsonify({"code": 200, "msg": "恭喜，调用成功！"})
    else:
        return jsonify({"code": 2001, "msg": "主键/视频设备ID/智能算法ID不能为空，请检查！！！"})


@app.route("/update", methods=['POST'])
def video_update():
    id = request.json.get("id").strip()  # 主键（业务ID）
    devID = request.json.get("devID").strip()  # 视频设备ID
    algID = request.json.get("algID").strip()  # 智能算法ID
    staTime = request.json.get("staTime", datetime.datetime.now().strftime('%T')).strip()  # 开始时间，当天时间，默认为当前时间
    endTime = request.json.get("endTime", "24:00:00").strip()  # 结束时间，当天时间，默认为24:00:00
    repPeriod = request.json.get("repPeriod", 1)  # 重复周期，正整数，默认为1，表示一天
    repNumber = request.json.get("endTime", 1)  # 重复次数，非正数时表示永久重复，默认为1
    priority = request.json.get("priority", 0)  # 优先级，默认为0
    comments = request.json.get("comments", "").strip()  # 备注

    tmp = []
    with open('business_data.txt', 'r') as f:
        for line in f:
            tmp.append(json.loads(line))

    if id and devID and algID:
        for i in range(len(tmp)):
            if tmp[i]["id"] == id:
                staTime_list = staTime.split(':')
                staTime_data = [int(x) for x in staTime_list]
                SH = staTime_data[0]
                SM = staTime_data[1]
                SS = staTime_data[2]
                endTime_list = endTime.split(':')
                endTime_data = [int(x) for x in endTime_list]
                EH = endTime_data[0]
                EM = endTime_data[1]
                ES = endTime_data[2]
                if not ((SH >= 0) and (SH < 24) and (SM >= 0) and (SM < 60) and (SS >= 0) and (SS < 60)):
                    return jsonify({"code": 2002, "msg": "开始时间输入格式不正确！！！"})
                elif not ((EH >= 0) and (EH < 24) and (EM >= 0) and (EM < 60) and (ES >= 0) and (
                        ES < 60) and endTime != "24:00:00"):
                    return jsonify({"code": 2003, "msg": "结束时间输入格式不正确！！！"})
                elif staTime >= endTime:
                    return jsonify({"code": 2004, "msg": "开始时间早于结束时间，请检查！！！"})
                elif priority < 0 or priority > 9:
                    return jsonify({"code": 2005, "msg": "优先级最低为0，最高为9，输入不正确，请检查！！！"})
                else:
                    s = {"id": id, "devID": devID, "algID": algID, "staTime": staTime, "endTime": endTime,
                         "repPeriod": repPeriod, "repNumber": repNumber, "priority": priority, "comments": comments}
                    aa = json.dumps(s, ensure_ascii=False)
                    with open(r"business_data.txt", "a") as f:
                        f.write(aa + '\n')
                    return jsonify({"code": 200, "msg": "恭喜，调用成功！"})

                return jsonify({"code": "200", "msg": "操作成功"})
            else:
                return jsonify({"code": "2006", "msg": "不存在该业务数据，请检查！！！"})

    else:
        return jsonify({"code": 2001, "msg": "主键/视频设备ID/智能算法ID不能为空，请检查！！！"})

@app.route("/delete", methods=['POST'])
def video_delete():
    id = request.json.get("id").strip()  # 主键（业务ID）
    comments = request.json.get("comments", "").strip()  # 备注
    tmp = []
    with open('business_data.txt', 'r') as f:
        for line in f:
            tmp.append(json.loads(line))
    if id:
        for i in range(len(tmp)):
            if tmp[i]["id"] == id:
                return jsonify({"code": "200", "msg": "操作成功"})
            else:
                return jsonify({"code": "2006", "msg": "不存在该业务数据，请检查！！！"})
    else:
        return jsonify({"code": 2001, "msg": "主键不能为空，请检查！！！"})

@app.route("/query", methods=['POST'])
def video_query():
    id = request.json.get("id").strip()  # 主键（业务ID）
    comments = request.json.get("comments", "").strip()  # 备注
    tmp = []
    with open('business_data.txt', 'r') as f:
        for line in f:
            tmp.append(json.loads(line))
    if id:
        for i in range(len(tmp)):
            if tmp[i]["id"] == id:
                return jsonify({"code": "200", "data": tmp[i], "msg": "操作成功"})
            else:
                return jsonify({"code": "2006", "msg": "不存在该业务数据，请检查！！！"})
    else:
        """获取所有用户信息"""
        tmp = []
        return jsonify({"code": "200", "data": tmp, "msg": "操作成功"})


if __name__ == '__main__':
    app.run()
