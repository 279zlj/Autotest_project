<template>
  <div class="row" id="table_data">
    <div class="col-lg-11 col-md-11 col-sm-11 col-xs-11">
      <div class="row modal-title">
        <p class="font-p">数据一览</p>
      </div>
      <div class="modal-body table-bordered">
        <div class="modal-header row">
          <div class="col-lg-2 col-md-3 col-sm-3 col-xs-2">
            <h4 >服务器信息</h4 >
          </div>
          <div class="col-lg-1 col-lg-offset-7 col-md-1 col-md-offset-2 col-sm-1 col-sm-offset-5 col-xs-2 " >
            <button type="button" class="btn btn-success" id="testbtn" v-on:click="stra()" >测试</button>
          </div>
          <div class="col-lg-1 col-md-1  col-sm-1  col-xs-2 " >
            <input type="button" class="btn btn-success " id="again" name="again" value="重测"  @click="checkagain(1)"></input>
          </div>
          <div class="col-lg-1 col-md-2  col-sm-1  col-xs-2 ">
            <el-button class="btn btn-danger" type="primary" @click="exportTable()">导出Excel</el-button>
          </div>
        </div>

        <table class="table table-responsive table-hover" style="table-layout: fixed">
          <thead>
          <th v-for="item in list"><span :class="item.ic" class="minicon"></span>{{item.title}}</th>
          </thead>
          <colgroup>
            <col style="width: 4%"/>
            <col style="width: 13%"/>
            <col style="width: 13%"/>
            <col style="width: 13%"/>
            <col style="width: 13%"/>
            <col style="width: 13%"/>
            <col style="width: 11%"/>
            <col style="width: 20%"/>
          </colgroup>
          <tbody>
          <tr v-for="(i,k) in d">
            <td><input type="checkbox" class="checkbox" v-model="i.checkstate" name="checkone" id="checknum"  @click="checkitem(k)"></td><td>{{i.server_num}}</td><td>{{i.cpu}}</td><td>{{i.memory_bank}}</td><td>{{i.hard_disk}}</td>
            <td>{{i.board}}</td><td><span class="label " :class="i.state=='数据有误'?'label-danger':'label-success'" v-model="i.state">{{i.state}}</span></td>
            <td>
              <button class="btn btn-info btn-sm" id="detail" data-toggle="modal" data-target="#myModal" v-bind:value="k"  @click="detail_num(k)">查看详情</button>
              <button class="btn btn-info btn-sm" id="o_data" data-toggle="modal" data-target="#myModalold" v-bind:value="k"  @click="old_num(i.server_num)" :class="i.state=='老化测试中'||i.state=='老化测试完成'?'':'no'">老化结果</button>
            </td>
          </tr>

          </tbody>
        </table>
        <div class="row" id="opr">
          <div class="col-lg-1 col-md-1 col-sm-2 col-xs-2">
            <input type="button" class="btn btn-primary btn-sm" v-on:click='checkall()' id="checkallname" name="checkallname" value="全选">
          </div>
          <div class="col-lg-1 col-md-1 col-sm-2 col-xs-2">
            <input type="button" class="btn btn-primary btn-sm" id="checkrevstate" v-on:click='checkrev()' name="checkrevstate" value="反选">
          </div>
          <div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">
            <input type="button" class="btn btn-primary btn-sm" id="checkno" v-on:click='checknot()' name="checkno" value="全不选">
          </div>
          <div class="col-lg-2 col-md-2 col-sm-2 col-xs-3">
            <select class="sele" @click="search_sys()" v-on:change="indexsel($event)" v-model="sel">
              <option value="none" >請選擇系統</option>
              <option v-for="s in system" :value="s.val" class="selec">{{s.sysname}}</option>
            </select>
          </div>
          <div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">
            <input type="button" class="btn btn-primary btn-sm" id="insta" v-on:click='checkagain(2)' name="insta" value="安装系统">
          </div>
          <div class="col-lg-2 col-lg-offset-1 col-md-2 col-md-offset-0 col-sm-3 col-xs-3 fontn">
            共<span>{{d.length}}</span>台
          </div>
        </div>

        <!-- 详情模态框（Modal） -->
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="" id="myModalLabel">
                  详细信息如下：
                </h4>
              </div>
              <div class="modal-body row">
                <p class="t">测试数据：</p>
                <div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">
                  <div v-for="item in list_detail">
                    <div class="fontp">{{item}}</div>
                  </div>
                </div>
                <div class="col-lg-10 col-md-10 col-sm-10 col-xs-10">

                    <div class="fontp">{{i.server_num}}</div>
                    <div class="fontp">{{i.cpu}}</div>
                    <div class="fontp">{{i.memory_bank}}</div>
                    <div class="fontp">{{i.hard_disk}}</div>
                    <div class="fontp">{{i.board}}</div>
                    <div class="fontp">{{i.raid}}</div>
                    <div class="fontp">{{i.vga}}</div>
                    <div class="fontp">{{i.gpu}}</div>
                    <div class="fontp">{{i.hba}}</div>
                    <div class="fontp">{{i.net_card}}</div>
                    <div class="fontp">{{i.fc_card}}</div>
                    <div class="fontp">{{i.status}}</div>
                    <div class="fontp">{{i.ip_info}}</div>

                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="all(1,i.server_num)" >
                数据有误
                </button>
                <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="all(2,i.ip_info)" id="old_data">
                  开始老化
                </button>
              </div>
            </div><!-- /.modal-content -->
          </div><!-- /.modal -->
        </div><!-- /.modal-end-->
      <!-- 老化模态框（Modal） -->
        <div class="modal fade" id="myModalold" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="" id="myModalLabel">
                  详细信息如下：
                </h4>
              </div>
              <div class="modal-body row">
                <p class="t">老化数据：</p>

                <div class="col-lg-10 col-md-10 col-sm-10 col-xs-10">
                  <div>
                    <div class="fontp">{{old}}</div>
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary" data-dismiss="modal" >
                  确定
                </button>
              </div>
            </div><!-- /.modal-content -->
          </div><!-- /.modal -->
        </div><!-- /.modal-end-->
      </div>
    </div>
  </div>

</template>

<script>

  import {getArr} from '../mock/api'

  export default {
    name: "table_data",
    inject:['reload'],
    data:function(){
      return {
         websock:null,
        labelstate:1,
        i:{},
        d:[],
        ct:[],
        ins:[],
        ri:[],
        sel:{},
        list:[
          {title:'',ic:'glyphicon glyphicon-edit'},
          {title: '序列号',ic:'glyphicon glyphicon-list'},
          {title: 'CPU',ic:'glyphicon glyphicon-stop'},
          {title: '内存',ic:'glyphicon glyphicon-file'},
          {title: '硬盘',ic:'glyphicon glyphicon-hdd'},
          {title: '主板',ic:'glyphicon glyphicon-inbox'},
          {title: 'state',ic:'glyphicon glyphicon-tags'},
          {title:'操作',ic:'glyphicon glyphicon-wrench'}
        ],
        list_detail: {
          num: '序列号',
          cpu: 'CPU',
          memory: '内存',
          disk: '硬盘',
          board: '主板',
          array: '阵列',
          Videocar: '显卡',
          GPU: 'GPU',
          HBA: 'HBA',
          network:'网卡',
          opticalcar:'光纤卡',
          state:"状态",
          ip:"ip",
          check:"是否选中"
        },
        system:[],
        checkarr:[],
        checka:{},
        state:false,
        old:[],
        h:[],

      }
    },

    mounted() {
      // axios请求，可换成http
      // var url=this.HOME+'test.json'
      //this.$axios.get('http://localhost:8081/api/test').then((res) => {
       // this.d=res.data
       // console.log( '请求成功')
      //}, (err) => {
       // console.log(err, '请求失败');
      //});
       this.initWebSocket();

    },
    destroyed(){
       this.websock.close();
    },

    methods:{
      stra:function(){
        this.$axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
        for (let i in this.d){
          if (this.d[i].state=="重测中"||this.d[i].state=="老化测试中"||this.d[i].state=="安装系统中") {
            this.ri.push(this.d[i].num)
          }
        }
        console.log(this.ri)
        if (this.ri.length>0){
          alert(this.ri+'处于正在重测、老化测试或安装系统中，请稍后再试')
        }
        //else if (this.d.length>0){
          //this.d.splice(0)
        //}
        else {
          this.$axios.post('http://localhost:8000/auto/start_running/', 'test_start').then(function (res) {
           let r=res.data.feedback
              console.log(r)
              if(r.length>0){
                alert(r+'沒有連接上')
              }
              else{
                alert('機器已全部上線')
              }
          })
            .catch(function (error) {
              console.log(error)
            })
        }
      },
      all(tip_state,ifstate){
        if (tip_state==1) {
          this.i.state='数据有误'
          this.$axios.post('http://localhost:8000/auto/change_status/',ifstate).then(function (res) {
            alert(res.data.feedback)
          })
            .catch(function (error) {
              console.log(error)
            })
        }
        if (tip_state==2) {
          if (this.i.state == '重测中') {
            alert('重测中，无法进行老化测试')
          }
          else {
            this.i.state = '老化测试中'
            this.$axios.post('http://localhost:8000/auto/begin_test/', {opr: 'old_start', ip: ifstate}).then(function (res) {
              alert(res.data.feedback)
            })
              .catch(function (error) {
                console.log(error)
              })
          }
        }
      },
      old_num(num){
      console.log(num)
      var _this=this

        this.$axios.post('http://localhost:8000/auto/search_aging_test/',num).then(function (res) {
        if(res.data.feedback.length>0)
        {
          _this.old=res.data.feedback
          _this.i.state='老化测试完成'

          }
        else
         _this.old='老化测试尚未完成'
          console.log(res.data.feedback,this.old)
        })
          .catch(function (error) {
            console.log(error)
          })
      },
      // 分页组件传回的表格数据
      // data(data) {
      //   this.tableList = data
      //   console.log('tableList',this.tableList)
      // },

      detail_num:function (a) {
        this.i=this.d[a]

      },
      checkitem:function (k) {
        if (!(this.d[k].checkstate)) {
          this.d[k].checkstate=true
          this.checka[this.d[k].ip_info]=this.d[k].server_num
          this.checkarr.push(this.checka)
          console.log(this.checkarr)
        }else {
          this.d[k].checkstate=false
          var b=this.checkarr.indexOf(this.d[k].ip_info)
          this.checkarr.splice(b,1)
          console.log(this.checkarr)
        }
      },
      checkall:function () {
        this.checkarr.splice(0)
        for (let i in this.d) {
          this.d[i].checkstate=true
          this.checka[this.d[i].ip_info]=this.d[i].server_num
          this.checkarr.push(this.checka)
        }
        console.log(this.checkarr)
      },
      checkrev:function () {
        this.checkarr.splice(0)
        for (let i in this.d){
          if(this.d[i].checkstate){
            this.d[i].checkstate=false
          }
          else {
            this.d[i].checkstate=true
            this.checka[this.d[i].ip_info]=this.d[i].server_num
          this.checkarr.push(this.checka)
          }
        }
        console.log(this.checkarr)
      },
      checknot:function(){
        for (let i in this.d){
          this.d[i].checkstate=false
        }
        this.checkarr.splice(0)
        console.log(this.checkarr)
      },
      checkagain:function (num) {
        if (this.checkarr.length==0){
          alert('没有选择机器')
        }
        else {

          if (num == 1) {
          this.ct.splice(0)

            for (let i in this.checkarr) {

              for (let p in this.d) {
              for (let key in this.checkarr[i]){
                var a=key
              }

                if (a == this.d[p].ip_info&&this.d[p].state != "安装系统中"&&this.d[p].state != "老化测试中")
                  {

                      this.d[p].state = "重测中"

                      console.log('again_test')
                  }

                else if ((this.d[p].state === "老化测试中"||this.d[p].state==="安装系统中")&&(a == this.d[p].ip_info)) {
                  this.ct.push(this.d[p].num)
                  console.log(this.ct)
                }

              }
            }
            if (this.ct.length > 0) {
              alert(this.ct + '正在老化测试或安装中，暂时无法重测')
            }
            console.log(this.checkarr)
            this.$axios.post('http://localhost:8000/auto/restart_running/', this.checkarr).then(function (res) {
              let r=res.data.feedback
              console.log(r)
              if(r.length>0){
                alert(r+'沒有連接上')
                this.checkarr.splice(0)
              }
              else{
                alert('所選機器正在重测')
                this.checkarr.splice(0)
              }
            })
              .catch(function (error) {
                console.log(error)
              })

          }
          if (num == 2) {
          if (typeof (this.sel)=="object"||this.sel=='none'){
              alert('请选择系统')
            }
            this.ins.splice(0)
            for (let i in this.checkarr) {

              for (let p in this.d) {
              for (let key in this.checkarr[i]){
                var a=key
              }


              if ((a == this.d[p].ip_info) &&(this.d[p].state != "老化测试中")&&(this.d[p].state != "重测中")){

                  this.d[p].state = "安装系统中"
                  }

              else if ((this.d[p].state === "老化测试中"||this.d[p].state==="重测中")&&(a == this.d[p].ip_info)) {
                this.ins.push(this.d[p].num)

              }
            }
            }
            if (this.ins.length > 0) {
              alert(this.ins + '正在老化测试或重测中，暂时无法安装')

            }

            this.$axios.post('http://localhost:8000/auto/install_system/', {sel:this.sel,ip: this.checkarr}).then(function (res) {
              let r=res.data.feedback
              console.log(r)
              if(r.length>0){
                alert(r+'沒有連接上')
                this.checkarr.splice(0)
              }
              else{
                alert('所選機器正在安装')
                this.checkarr.splice(0)
              }
              this.checkarr.splice(0)
            })
              .catch(function (error) {
                console.log(error)
              })

          }
        }
      },
      // ta:function() {
      //   let obj= '{"num": "001","cpu": "aaa","memory": "123","disk": "dsaf","ssd": "dsfds","board": "fsd","radiator": "ewq23","chassis": "wet45","panel": "54fret","state": "rwe34"}'
      //   this.d.unshift( JSON.parse(obj))
      // },
      initWebSocket(){
        const wsurl="ws://127.0.0.1:8000/echo";
        this.websock=new WebSocket(wsurl);
        this.websock.onmessage=this.websocketonmessage;
        this.websock.onopen=this.websocketonopen;
        this.websock.websocket =this.websocket;
        this.websock.onclose=this.websocketclose;
      },
      websocketonopen(){
        console.log('ok')
        //console.log(JSON.parse(obj))
      },
      websocket(){
        this.initWebSocket()
      },
      websocketonmessage(e){
        const redata=JSON.parse(e.data)
        this.h.splice(0)
        if(this.d.length==1){
          for (let i in this.d){
            if(this.d[i].server_num==redata.server_num){
              this.$set(this.d,i,redata)

              break
            }
            else{
              this.d.push(redata)

              break
              }
          }
        }

        else if(this.d.length>2||this.d.length==2){

            for (let i in this.d){

            if(this.d[i].server_num===redata.server_num){
              this.$set(this.d,i,redata)
              break
            }

            else if(this.d[i].server_num!=redata.server_num){
              this.h.push(redata)

              continue
            }

            }
          console.log(this.h.length,this.d.length)
          if(this.h.length==this.d.length){
            this.d.push(redata)
            this.h.splice(0)
          }
        }
        if(this.d.length===0){
          this.d.push(redata)
        }

      },
      websocketsend(Data){
        console.log(Data)

      },
      websocketclose(e){
        console.log('断开连接',e);
      },

    indexsel:function(event){//下拉框选择
        this.sel=event.target.value
      },
      search_sys:function () {
        this.system.splice(1,)
        this.$axios.get('http://localhost:8000/auto/search_system_list/').then((res) => {
          this.system=res.data.feedback
          console.log(this.system)
        }, (err) => {
          console.log(err);
        });
      },

exportTable() {
        require.ensure([], () => {
          const { export_json_to_excel } = require('../assets/excel/Export2Excel');
          const tHeader = ['系列号', 'CPU', '内存', '硬盘','主板','阵列', '显卡', 'GPU', 'HBA','网卡', '光纤卡'];
          const filterVal = ['server_num', 'cpu', 'memory_bank', 'hard_disk','board', 'raid', 'vga', 'gpu','hba', 'net_card', 'fc_card'];
          const list = this.d;
          const data = this.formatJson(filterVal, list);
          export_json_to_excel(tHeader, data, '测试机结果');
          })
        },
        formatJson(filterVal, jsonData) {
          return jsonData.map(v => filterVal.map(j => v[j]))
        }
},
  }
</script>

<style scoped>
.no{
  display:none
}
.selec{
  width:120px;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
  .sele{
    width:120px;
    line-height: 2em;
    font-size: 1.1em;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
  }
  .fontn{
    font-size: 1.3em;

  }
  .fontp{
    width:40em;
    height:1.5em;
  }
  .st{
    display: none;
  }
  .minicon{
    margin-right:.5em
  }
  .t{
    text-align: left;
    margin-left: 1em;
    font-weight: 700;
    font-size: 1.2em;
    line-height: 2em;
  }
  .container
  {
    height: 100%;

  }
  .modal-title{
    background-color:#F8F8F8 ;
    margin:1.5em 0 2em 0;
    height: 4em;
    border-radius: .5em;
  }
  .font-p{
    font-size: 1.5em;
    line-height: 2.5em;
    margin-left: 1em;
    color: #4A4949;
  }
  .table{
    margin-top: 1em;

  }
  #table_data{
    padding-bottom: 2em;
  }
  th,td{
    text-align: center;
    overflow: hidden;text-overflow: ellipsis;white-space: nowrap;
  }
  th{
    font-size: 1.1em;
  }
  @media screen and (max-width: 768px) {
    .re {
      margin-left: 1.5em;
    }
  }
</style>
