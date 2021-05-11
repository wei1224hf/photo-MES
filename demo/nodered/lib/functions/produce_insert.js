// name: 新增生产安排
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 
msg.payloads.push(msg.payload);
msg.topics.push(msg.topic);

let uuid = global.get('uuid');
let db = msg.db;
db['id'] = uuid.v4();
keys = [];
values = [];

if(db['code']){
    keys.push("code");
    values.push("'"+db['code']+"'");
}
if(db['name']){
    keys.push("name");
    values.push("'"+db['name']+"'");
}
if(db['id']){
    keys.push("id");
    values.push("'"+db['id']+"'");
}
if(db['time_start']){
    keys.push("time_start");
    values.push("'"+db['time_start']+"'");
}
if(db['time_done']){
    keys.push("time_done");
    values.push("'"+db['time_done']+"'");
}
if(db['product']){
    keys.push("product");
    values.push("'"+db['product']+"'");
}
if(db['user_qc']){
    keys.push("user_qc");
    values.push("'"+db['user_qc']+"'");
    keys.push("creater_id");
    values.push("'"+db['user_qc']+"'");
    keys.push("updater_id");
    values.push("'"+db['user_qc']+"'");    
    keys.push("creater_group");
    values.push("(select group_code from basic_user where id = '"+db['user_qc']+"')");       
}
if(db['user_planner']){
    keys.push("user_planner");
    values.push("'"+db['user_planner']+"'");
}
if(db['user_check']){
    keys.push("user_check");
    values.push("'"+db['user_check']+"'");
}
if(db['user_process']){
    keys.push("user_process");
    values.push("'"+db['user_process']+"'");
}
if(db['user_manager']){
    keys.push("user_manager");
    values.push("'"+db['user_manager']+"'");
}
if(db['user_planer']){
    keys.push("user_planner");
    values.push("'"+db['user_planer']+"'");
}
if(db['num_plan']){
    keys.push("num_plan");
    values.push("'"+db['num_plan']+"'");
}
if(db['bag']){
    keys.push("num_box");
    values.push("'"+db['bag']+"'");
}
if(db['class']){
    keys.push("class");
    values.push("'"+db['class']+"'");
}
if(db['production']){
    keys.push("num_production");
    values.push("'"+db['production']+"'");
}
if(db['status']){
    keys.push("status");
    values.push("'"+db['status']+"'");
}

if(true){
    keys.push("time_created");
    values.push("now()");
    keys.push("time_lastupdated");
    values.push("now()");    
    keys.push("count_updated");
    values.push("1");    
    keys.push("type");
    values.push("1");       
}

let sql = "insert into produce (";
let sql2 = ")values(";
sql += keys.join(",");
sql2 += values.join(",");
sql = sql+sql2+");";
msg.topic = sql;
msg.uuid = db['id'];
return msg;