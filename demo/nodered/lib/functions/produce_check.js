// name: 数据检查
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 
let db = msg.db;
let connection = msg.conn;
var err = false;
let errors = '';

var awaitDB = global.get("awaitDB");
var aDB = awaitDB(connection);

try{
	if( db['qc']){
		var results = aDB.query("SELECT * from basic_user where username = '"+db['qc']+"'");
		if(results.length==0){
			err = true;
			errors += ',no qc'+db['qc'];
		}
		else{
			delete(db['qc']);
			db['user_qc'] = results[0].id;
		}
	}

	if( db['planer']){
		var results = aDB.query("SELECT * from basic_user where username = '"+db['planer']+"'");
		if(results.length==0){
			err = true;
			errors += ',no planer'+db['planer'];
		}
		else{
			delete(db['planer']);
			db['user_planer'] = results[0].id;
		}
	}

	if( db['process']){
		var results = aDB.query("SELECT * from basic_user where username = '"+db['process']+"'");
		if(results.length==0){
			err = true;
			errors += ',no process'+db['process'];
		}
		else{
			delete(db['process']);
			db['user_process'] = results[0].id;
		}
	}

	if( db['manager']){
		var results = aDB.query("SELECT * from basic_user where username = '"+db['manager']+"'");
		if(results.length==0){
			err = true;
			errors += ',no manager'+db['manager'];
		}
		else{
			delete(db['manager']);
			db['user_manager'] = results[0].id;
		}
	}

	if( db['check']){
		var results = aDB.query("SELECT * from basic_user where username = '"+db['check']+"'");
		if(results.length==0){
			err = true;
			errors += ',no check'+db['check'];
		}
		else{
			delete(db['check']);
			db['user_check'] = results[0].id;
		}
	}

	if( db['product']){
		var results = aDB.query("SELECT * from rd_product where code = '"+db['product']+"'");
		if(results.length==0){
			err = true;
			errors += ',no product'+db['product'];
		}
		else{
			delete(db['product']);
			db['product'] = results[0].id;
			db['name'] = results[0].name+'_拍摄导入';
		}
	}

	var stations = [];
	for(var i2=1;i2<=12;i2++){
		var station = {};
		if( db['device--'+i2]){
			var results = aDB.query("SELECT * from device where code = '"+db['device--'+i2]+"'");
			if(results.length==0){
				err = true;
				errors += ',no device'+db['device--'+i2];
			}
			else{
				delete(db['device--'+i2]);
				station['d'] = results[0].id;

				if( !(db['worker--'+i2]) ){
					err = true;
					errors += ',need worker '+i2;
				}
				else{
					var results2 = aDB.query("SELECT * from basic_user where username = '"+db['worker--'+i2]+"'");
					if(results.length==0){
						err = true;
						errors += ',no worker '+db['worker--'+i2];
					}
					else{
						delete(db['worker--'+i2]);
						station['w'] = results[0].id;
						station['job'] = '组长';

						if( !(db['production--'+i2]) ){
							err = true;
							errors += ',need production '+i2;
						}
						else{  
							station['num_production'] = db['production--'+i2];
							delete(db['production--'+i2]);
						} 
						if( (db['bad--1']) ){  
							station['num_bad'] = db['bad--'+i2];
							delete(db['bad--'+i2]);
						}
						if( (db['back--'+i2]) ){  
							station['num_back'] = db['back--'+i2];
							delete(db['back--'+i2]);
						}
						stations.push(station);  
					}
				}	
			}
		}
	}
} catch ( err ) {

} finally {
  
}

msg.stations = stations;
msg.err = err;
if(err){
	msg.errors = errors;
}
return msg;


