<template>
  <div class="row" id="search">
    <div class="col-lg-11 col-md-11 col-sm-11 col-xs-11">
      <div class="row modal-title">
        <p class="font-p">历史数据查询</p>
      </div>
      <div class="modal-body table-bordered">
        <div class="modal-header row">

          <div class="col-lg-2 col-md-2 col-sm-3 col-xs-2">
            <h4>历史信息</h4>
          </div>
          <div class="col-lg-3 col-lg-offset-5 col-md-4 col-md-offset-3 col-sm-4 col-sm-offset-3 col-xs-6 col-xs-offset-0">

            <div class="form-group has-feedback" >

              <input type="search" class="form-control fc-clear" id="search" ref="wordkey" autofocus  placeholder="请输入序列号查询"/>
            </div>
          </div>
          <div class="col-lg-1 col-md-2 col-sm-2 col-xs-1">
            <button type="button" class="btn btn-success" @click="out()">搜索</button>
          </div>

        </div>


        <table class="table table-responsive table-hover" style="table-layout: fixed">
          <thead>
          <th v-for="item in list"><span :class="item.ic" class="minicon"></span>{{item.title}}</th>
           </thead>
          <tbody>
          <tr v-for="(i,k) in selectdata">
            <td>{{i.num}}</td><td>{{i.cpu}}</td><td>{{i.memory}}</td><td>{{i.disk}}</td>
            <td>
              <button class="btn btn-info btn-sm" id="detail" data-toggle="modal" data-target="#myModal" v-bind:value="k"  @click="detail_num(k)">查看详情</button>
              <button class="btn btn-info btn-sm" id="o_data" data-toggle="modal" data-target="#myModalold" v-bind:value="k"  @click="old_num(i.server_num)" >老化结果</button>
            </td>
          </tr>

          </tbody>
        </table>

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
                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                  <div v-for="item in list_detail">
                    <div class="fontp">{{item}}</div>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                  <div v-for="a in i" >
                    <div class="fontp" >{{a}}</div>
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="all(1,i.num)" >
                  数据有误
                </button>
                <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="all(2,i.ip)" id="old_data">
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
                <p class="t">测试数据：</p>
                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                  <div>
                    <div class="fontp"></div>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                  <div>
                    <div class="fontp" ></div>
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
  export default {
    name: "search",
    data(){
      return {
        list: [
          {title: '序列号',ic:'glyphicon glyphicon-list'},
          {title: 'CPU',ic:'glyphicon glyphicon-stop'},
          {title: '内存',ic:'glyphicon glyphicon-file'},
          {title: '硬盘',ic:'glyphicon glyphicon-hdd'},

          {title:'操作',ic:'glyphicon glyphicon-wrench'}
        ],
        selectdata:[]
      }
    },
    methods: {
      out: function () {
      this.$axios.post('http://localhost:8000/auto/search/', {server_num: this.$refs.wordkey.value}).then(function (res) {
              this.selectdata=res.data
              console.log(res)
            })
              .catch(function (error) {
                console.log(error)
              })

      },


    }
  }
</script>

<style scoped>
  .one{
    display: none;
  }
  .minicon{
    margin-right:0.5em
  }
  @media screen and (max-width: 768px){

    .t{
      font-size: .8em;

    }
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
  th{
    text-align: center;
  }
</style>
