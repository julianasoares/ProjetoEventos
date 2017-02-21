from django.db import models
from django.contrib.auth.models import User

# Modelo pacote
#class Tipo_pacote(models.Model):
 #   desc_pacote = models.CharField("Tipo de pacote", max_length=50)
  #  quant_pessoas = models.IntegerField("Quantidade de Pessoas",null=False,blank=False)
   # quant_horas = models.FloatField("Quantidade de Horas",null=False,blank=False)
    #valor_total_estimado = models.FloatField("Valor do Pacote",null=False,blank=False)
    #pacote_ativo = models.BooleanField("Situação do pacote")


# modelo itens
class Item(models.Model):
    descricaoItem = models.CharField("Descricao", max_length=50)
    tipoItem = models.CharField("Tipo do Item", max_length=50)
    valorItem = models.FloatField("Valor Item",null=False,blank=False)
    #pacote = models.ManyToManyField(Tipo_pacote,through="Pacote_itens")

    def __str__(self):
        return self.descricaoItem

# modelo pacote_itens
#class Pacote_itens(models.Model):
#    cod_tipo_pacote = models.ForeignKey(Tipo_pacote, on_delete=models.CASCADE)
  #  cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
   # valor_item_pacote = models.FloatField("Valor Item Pacote",null=False,blank=False)
    #quant_item_pacote = models.FloatField("Quantidade Item Pacote",null=False,blank=False)
    #valor_hora_extra = models.FloatField("Valor Hora Extra",null=False,blank=False)

class Cliente(User):
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False, blank=False)
    telefone1 = models.CharField("Telefone 1", max_length=11, blank=True, null=True)
    telefone2 = models.CharField("Telefone 2", max_length=11, blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=255)

    def __str__(self):
        return self.first_name + self.last_name


# modelo forma de pagamento do Evento
class FormaPagamento(models.Model):
    descricaoFormaPagamento = models.CharField("Descrição Forma de Pagamento", max_length=14, null=False, blank=False)

    def __str__(self):
        return self.descricaoFormaPagamento


# Modelo tipo de Evento
class TipoEvento(models.Model):
    descricaoEvento = models.CharField("Descricao", max_length=50)

    def __str__(self):
        return self.descricaoEvento


# Modelo situação
class SituacaoEvento(models.Model):
    tipoSituacao = models.CharField("Situação", max_length=150, null=False)

    def __str__(self):
        return self.tipoSituacao


# Modelo Evento
class Evento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="Cliente", null=False)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT, verbose_name="Tipo de Evento", null=False)
    #tipo_pacote = models.ForeignKey(Tipo_pacote, on_delete=models.PROTECT, verbose_name="Tipo de Pacote", null=False)
    dataEvento = models.DateField("Data do Evento", null=True, blank=True, editable=True)
    dataSolicitacao = models.DateTimeField("Data da solicitação", null=True, blank=True, auto_now_add=True, editable=False)
    tipoSituacao = models.ForeignKey(SituacaoEvento, max_length=50, blank=True, null=True, default=1)
    item = models.ManyToManyField(Item, through="EventoItem")
    formaPagamento = models.ManyToManyField(FormaPagamento,through="EventoFormaPagamento")
    quantPessoas = models.IntegerField("Quantidade de Pessoas", null=False,blank=False)
    horaExtra = models.FloatField("Hora Extra",null=True,blank=True)

class OrcamentoEvento(models.Model):
    nome = models.CharField("Nome", max_length=255, null=False, blank=False)
    email = models.EmailField("E-mail",null=False,blank=False)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False, blank=False)
    telefone1 = models.CharField("Telefone 1", max_length=11, blank=False, null=False)
    telefone2 = models.CharField("Telefone 2", max_length=11, blank=True, null=True)
    rua = models.CharField("Rua", max_length=255,blank=False, null=False)
    numero = models.IntegerField("Nº",blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=255,blank=False, null=False)
    cidade = models.CharField("Cidade", max_length=255,blank=False, null=False)
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT, verbose_name="Tipo de Evento", null=False)
    dataEvento = models.DateField("Data do Evento", null=True, blank=True, editable=True)
    dataSolicitacao = models.DateTimeField("Data da solicitação", null=True, blank=True, auto_now_add=True, editable=False)
    tipoSituacao = models.ForeignKey(SituacaoEvento, max_length=50, blank=True, null=True, default=1)
    item = models.ManyToManyField(Item, through="OrcamentoEventoItem")
    formaPagamento = models.ManyToManyField(FormaPagamento,through="OrcamentoEventoFormaPagamento")
    quantPessoas = models.IntegerField("Quantidade de Pessoas", null=False,blank=False)
    horaExtra = models.FloatField("Hora Extra",null=True,blank=True)

# Modelo Relacionamento Evento e Item
class EventoItem(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete=models.PROTECT, verbose_name="Evento", null=False, blank=False)
    idItem = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name="Item", null=False, blank=False)
    valor = models.FloatField("Valor",null=False,blank=False)
    quantidade = models.IntegerField("Quantidade",null=False, blank=False)

# modelo Relacionamento Evento e Forma de Pagamento
class EventoFormaPagamento(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    idFormaPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    valorPago = models.FloatField("Valor Pago",null=False,blank=False)

# modelo Relacionamento OrçamentoEvento e Forma de Pagamento
class OrcamentoEventoItem(models.Model):
    idOrcamentoEvento = models.ForeignKey(OrcamentoEvento, on_delete=models.PROTECT, verbose_name="Orçamento Evento", null=False, blank=False)
    idItem = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name="Item", null=False, blank=False)
    valor = models.FloatField("Valor",null=False,blank=False)
    quantidade = models.IntegerField("Quantidade",null=False, blank=False)

# modelo Relacionamento OrçamentoEvento e Forma de Pagamento
class OrcamentoEventoFormaPagamento(models.Model):
    idOrcamentoEvento = models.ForeignKey(OrcamentoEvento, on_delete=models.CASCADE)
    idFormaPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    valorPago = models.FloatField("Valor Pago",null=False,blank=False)








