create table endereço(
	id_indereco serial primary key,
	cep varchar(50),
	quadra varchar(50),
	conjunto varchar(20),
	complemento varchar(50),
	bairro varchar(50),
	uf varchar(3));
	
create table usuario(
	telefone integer,
	email varchar(50),
	nome varchar(20),
	sobrenome varchar(20),
	senha varchar(50),
	id_endereco varchar(50)
	foreign key(id_endereco) references endereco(id_endereco)),
	id_metodo varchar(10),
	is_logado boolean,
	id_produtofav integer
	foreign key(id_produtosfav) references produtosfav(id_produtosfav));
	
create table pagamento(
	tp_cartao varchar(10),
	num_cartao integer,
	cvv integer,
	datadeexp data,
	nome_titular varchar (50));
	
create table hist_compra(
	id_user integer
	foreign key(id_user) references usuario(id_user),
	id_historico serial primary key,
	id_produto
	foreign key(id_produto) references produtos(id_produto),
	quantidade_comprada integer,
	valor integer,
	data_criacao data);
	
create table produtos(
	id_produtos serial primary key,
	nome varchar(50),
	qntd_estoque integer,
	fornecedor varchar(50),
	valor integer,
	especificacao varchar(20),
	categoria varchar(50),
	foto bytea);
	
create table carrinho(
	data_criacao data,
	id_carrinho serial primary key,
	valor_semdesc integer,
	valor_comdesc integer,
	id_carrinhoprod integer
	foreign key(id_carrinhoprod) references carrinhoprod(id_carrinhoprod));
	
create table categoria(
	id_cat serial primary key,
	nome varchar(10),
	desconto integer,
	data_cria data,
	is_ativada boolean);

create table cupom(
	id_cupom serial primary key,
	valor integer,
	data_cria data,
	categoria varchar (10),
	data_validade data);
	
create table produtosfav(
	id_prodfav serial primary key,
	data_favoritada data,
	id_user
	foreign key(id_user) references usuario(id_user),
	id_prod
	foreign key(id_prod) references produtos(id_prod),
	comprou boolean);

create table carrinhoprod(
	id_carrinhoprod serial primary key,
	id_carrinho
	foreign key(id_carrinho) references carrinho(id_carrinho),
	id_prod
	foreign key(id_prod) references produtos(id_prod),
	data_cria data,
	quantidade_comprada integer,
	presente boolean);
	
