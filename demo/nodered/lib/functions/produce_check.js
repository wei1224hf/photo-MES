// name: 数据检查
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 

let db = msg.db;
let connection = msg.conn;
var err = false;
let errors = '';

if( db['qc']){
	connection.query("SELECT * from basic_user where username = '"+db['qc']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no qc'+db['qc'];
		}
		else{
		    delete(db['qc']);
		    db['user_qc'] = results[0].id;
		}
	});
}


if( db['planer']){
	connection.query("SELECT * from basic_user where username = '"+db['planer']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no planer'+db['planer'];
		}
		else{
		    delete(db['planer']);
		    db['user_planer'] = results[0].id;
		}
	});
}

if( db['process']){
	connection.query("SELECT * from basic_user where username = '"+db['process']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no process'+db['process'];
		}
		else{
		    delete(db['process']);
		    db['user_process'] = results[0].id;
		}
	});
}

if( db['manager']){
	connection.query("SELECT * from basic_user where username = '"+db['manager']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no manager'+db['manager'];
		}
		else{
		    delete(db['manager']);
		    db['user_manager'] = results[0].id;
		}
	});
}

if( db['check']){
	connection.query("SELECT * from basic_user where username = '"+db['check']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no check'+db['check'];
		}
		else{
		    delete(db['check']);
		    db['user_check'] = results[0].id;
		}
	});
}

if( db['product']){
	connection.query("SELECT * from rd_product where code = '"+db['product']+"'", 
	function (error, results, fields) {
		if (error) console.debug(error); 
		if(results.length==0){
			err = true;
			errors += ',no product'+db['product'];
		}
		else{
		    delete(db['product']);
		    db['product'] = results[0].id;
		}
	});
}

var stations = [];

if( db['device--1']){
 connection.query("SELECT * from device where code = '"+db['device--1']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--1'];
  }
  else{
   delete(db['device--1']);
   station['d'] = results[0].id;
   
   if( !(db['worker--1']) ){
    err = true;
    errors += ',need worker 1';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--1']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--1'];
     }
     else{
      delete(db['worker--1']);
      station['w'] = results[0].id;
      station['job'] = '组长';
      
      if( !(db['production--1']) ){
       err = true;
       errors += ',need production 1';
      }
      else{  
       station['num_production'] = db['production--1'];
       delete(db['production--1']);
      } 
      if( (db['bad--1']) ){  
       station['num_bad'] = db['bad--1'];
       delete(db['bad--1']);
      }
      if( (db['back--1']) ){  
       station['num_back'] = db['back--1'];
       delete(db['back--1']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--2']){
 connection.query("SELECT * from device where code = '"+db['device--2']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--2'];
  }
  else{
   delete(db['device--2']);
   station['d'] = results[0].id;
   
   if( !(db['worker--2']) ){
    err = true;
    errors += ',need worker 2';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--2']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--2'];
     }
     else{
      delete(db['worker--2']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--2']) ){
       err = true;
       errors += ',need production 2';
      }
      else{  
       station['num_production'] = db['production--2'];
       delete(db['production--2']);
      } 
      if( (db['bad--2']) ){  
       station['num_bad'] = db['bad--2'];
       delete(db['bad--2']);
      }
      if( (db['back--2']) ){  
       station['num_back'] = db['back--2'];
       delete(db['back--2']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--3']){
 connection.query("SELECT * from device where code = '"+db['device--3']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--3'];
  }
  else{
   delete(db['device--3']);
   station['d'] = results[0].id;
   
   if( !(db['worker--3']) ){
    err = true;
    errors += ',need worker 3';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--3']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--3'];
     }
     else{
      delete(db['worker--3']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--3']) ){
       err = true;
       errors += ',need production 3';
      }
      else{  
       station['num_production'] = db['production--3'];
       delete(db['production--3']);
      } 
      if( (db['bad--3']) ){  
       station['num_bad'] = db['bad--3'];
       delete(db['bad--3']);
      }
      if( (db['back--3']) ){  
       station['num_back'] = db['back--3'];
       delete(db['back--3']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--4']){
 connection.query("SELECT * from device where code = '"+db['device--4']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--4'];
  }
  else{
   delete(db['device--4']);
   station['d'] = results[0].id;
   
   if( !(db['worker--4']) ){
    err = true;
    errors += ',need worker 4';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--4']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--4'];
     }
     else{
      delete(db['worker--4']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--4']) ){
       err = true;
       errors += ',need production 4';
      }
      else{  
       station['num_production'] = db['production--4'];
       delete(db['production--4']);
      } 
      if( (db['bad--4']) ){  
       station['num_bad'] = db['bad--4'];
       delete(db['bad--4']);
      }
      if( (db['back--4']) ){  
       station['num_back'] = db['back--4'];
       delete(db['back--4']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--5']){
 connection.query("SELECT * from device where code = '"+db['device--5']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--5'];
  }
  else{
   delete(db['device--5']);
   station['d'] = results[0].id;
   
   if( !(db['worker--5']) ){
    err = true;
    errors += ',need worker 5';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--5']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--5'];
     }
     else{
      delete(db['worker--5']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--5']) ){
       err = true;
       errors += ',need production 5';
      }
      else{  
       station['num_production'] = db['production--5'];
       delete(db['production--5']);
      } 
      if( (db['bad--5']) ){  
       station['num_bad'] = db['bad--5'];
       delete(db['bad--5']);
      }
      if( (db['back--5']) ){  
       station['num_back'] = db['back--5'];
       delete(db['back--5']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--6']){
 connection.query("SELECT * from device where code = '"+db['device--6']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--6'];
  }
  else{
   delete(db['device--6']);
   station['d'] = results[0].id;
   
   if( !(db['worker--6']) ){
    err = true;
    errors += ',need worker 6';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--6']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--6'];
     }
     else{
      delete(db['worker--6']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--6']) ){
       err = true;
       errors += ',need production 6';
      }
      else{  
       station['num_production'] = db['production--6'];
       delete(db['production--6']);
      } 
      if( (db['bad--6']) ){  
       station['num_bad'] = db['bad--6'];
       delete(db['bad--6']);
      }
      if( (db['back--6']) ){  
       station['num_back'] = db['back--6'];
       delete(db['back--6']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--7']){
 connection.query("SELECT * from device where code = '"+db['device--7']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--7'];
  }
  else{
   delete(db['device--7']);
   station['d'] = results[0].id;
   
   if( !(db['worker--7']) ){
    err = true;
    errors += ',need worker 7';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--7']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--7'];
     }
     else{
      delete(db['worker--7']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--7']) ){
       err = true;
       errors += ',need production 7';
      }
      else{  
       station['num_production'] = db['production--7'];
       delete(db['production--7']);
      } 
      if( (db['bad--7']) ){  
       station['num_bad'] = db['bad--7'];
       delete(db['bad--7']);
      }
      if( (db['back--7']) ){  
       station['num_back'] = db['back--7'];
       delete(db['back--7']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--8']){
 connection.query("SELECT * from device where code = '"+db['device--8']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--8'];
  }
  else{
   delete(db['device--8']);
   station['d'] = results[0].id;
   
   if( !(db['worker--8']) ){
    err = true;
    errors += ',need worker 8';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--8']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--8'];
     }
     else{
      delete(db['worker--8']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--8']) ){
       err = true;
       errors += ',need production 8';
      }
      else{  
       station['num_production'] = db['production--8'];
       delete(db['production--8']);
      } 
      if( (db['bad--8']) ){  
       station['num_bad'] = db['bad--8'];
       delete(db['bad--8']);
      }
      if( (db['back--8']) ){  
       station['num_back'] = db['back--8'];
       delete(db['back--8']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--9']){
 connection.query("SELECT * from device where code = '"+db['device--9']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--9'];
  }
  else{
   delete(db['device--9']);
   station['d'] = results[0].id;
   
   if( !(db['worker--9']) ){
    err = true;
    errors += ',need worker 9';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--9']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--9'];
     }
     else{
      delete(db['worker--9']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--9']) ){
       err = true;
       errors += ',need production 9';
      }
      else{  
       station['num_production'] = db['production--9'];
       delete(db['production--9']);
      } 
      if( (db['bad--9']) ){  
       station['num_bad'] = db['bad--9'];
       delete(db['bad--9']);
      }
      if( (db['back--9']) ){  
       station['num_back'] = db['back--9'];
       delete(db['back--9']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--10']){
 connection.query("SELECT * from device where code = '"+db['device--10']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--10'];
  }
  else{
   delete(db['device--10']);
   station['d'] = results[0].id;
   
   if( !(db['worker--10']) ){
    err = true;
    errors += ',need worker 10';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--10']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--10'];
     }
     else{
      delete(db['worker--10']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--10']) ){
       err = true;
       errors += ',need production 10';
      }
      else{  
       station['num_production'] = db['production--10'];
       delete(db['production--10']);
      } 
      if( (db['bad--10']) ){  
       station['num_bad'] = db['bad--10'];
       delete(db['bad--10']);
      }
      if( (db['back--10']) ){  
       station['num_back'] = db['back--10'];
       delete(db['back--10']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--11']){
 connection.query("SELECT * from device where code = '"+db['device--11']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--11'];
  }
  else{
   delete(db['device--11']);
   station['d'] = results[0].id;
   
   if( !(db['worker--11']) ){
    err = true;
    errors += ',need worker 11';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--11']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--11'];
     }
     else{
      delete(db['worker--11']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--11']) ){
       err = true;
       errors += ',need production 11';
      }
      else{  
       station['num_production'] = db['production--11'];
       delete(db['production--11']);
      } 
      if( (db['bad--11']) ){  
       station['num_bad'] = db['bad--11'];
       delete(db['bad--11']);
      }
      if( (db['back--11']) ){  
       station['num_back'] = db['back--11'];
       delete(db['back--11']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--12']){
 connection.query("SELECT * from device where code = '"+db['device--12']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--12'];
  }
  else{
   delete(db['device--12']);
   station['d'] = results[0].id;
   
   if( !(db['worker--12']) ){
    err = true;
    errors += ',need worker 12';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--12']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--12'];
     }
     else{
      delete(db['worker--12']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--12']) ){
       err = true;
       errors += ',need production 12';
      }
      else{  
       station['num_production'] = db['production--12'];
       delete(db['production--12']);
      } 
      if( (db['bad--12']) ){  
       station['num_bad'] = db['bad--12'];
       delete(db['bad--12']);
      }
      if( (db['back--12']) ){  
       station['num_back'] = db['back--12'];
       delete(db['back--12']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--13']){
 connection.query("SELECT * from device where code = '"+db['device--13']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--13'];
  }
  else{
   delete(db['device--13']);
   station['d'] = results[0].id;
   
   if( !(db['worker--13']) ){
    err = true;
    errors += ',need worker 13';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--13']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--13'];
     }
     else{
      delete(db['worker--13']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--13']) ){
       err = true;
       errors += ',need production 13';
      }
      else{  
       station['num_production'] = db['production--13'];
       delete(db['production--13']);
      } 
      if( (db['bad--13']) ){  
       station['num_bad'] = db['bad--13'];
       delete(db['bad--13']);
      }
      if( (db['back--13']) ){  
       station['num_back'] = db['back--13'];
       delete(db['back--13']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}
if( db['device--14']){
 connection.query("SELECT * from device where code = '"+db['device--14']+"'", 
 function (error, results, fields) {
  
  var station = {};
  if (error) console.debug(error); 
  if(results.length==0){
   err = true;
   errors += ',no device'+db['device--14'];
  }
  else{
   delete(db['device--14']);
   station['d'] = results[0].id;
   
   if( !(db['worker--14']) ){
    err = true;
    errors += ',need worker 14';
   }
   else{
    connection.query("SELECT * from basic_user where username = '"+db['worker--14']+"'", 
    function (error, results, fields) {
     if (error) console.debug(error); 
     if(results.length==0){
      err = true;
      errors += ',no worker '+db['worker--14'];
     }
     else{
      delete(db['worker--14']);
      station['w'] = results[0].id;
      station['job'] = '--';
      
      if( !(db['production--14']) ){
       err = true;
       errors += ',need production 14';
      }
      else{  
       station['num_production'] = db['production--14'];
       delete(db['production--14']);
      } 
      if( (db['bad--14']) ){  
       station['num_bad'] = db['bad--14'];
       delete(db['bad--14']);
      }
      if( (db['back--14']) ){  
       station['num_back'] = db['back--14'];
       delete(db['back--14']);
      }
      stations.push(station);     
      
     }
    });
   }    
   
  }
 });
}




msg.stations = stations;



setTimeout(function(){
	//connection.destroy();
	msg.err = err;
	if(err){
	    msg.errors = errors;
	}
	node.send( msg );
},1500);

