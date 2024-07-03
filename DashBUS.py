import streamlit as st
import pandas as pd

from io import BytesIO
import requests

from datetime import datetime
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib as mpl
#https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

def Grafico_MapaCalor(DFvalores, ListaLinhas, ListaColunas, LargPOL = 4, AltPOL = 5, Cor = 'Wistia'):
    # LargPOL = Largura da Figura em Polegadas
    # AltPOL = ALtura da Figura em Olegadas 
    
    #https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
    #https://matplotlib.org/stable/users/explain/colors/colormaps.html

    #Agora falta armazenar valores de aceleracao de cada motorista e depois colocar motoristas x Aceleração no HeatMap

    #ListaNomes = ['Nome1', 'Nome2', 'Nome3', 'Nome4', 'Nome5', 'Nome6']

    

    DFvalores = DFmat
    fig1, ax1 = plt.subplots(figsize=(LargPOL, AltPOL))
    plt.margins(0.2) 
    plt.subplots_adjust(bottom = 0.15) 

    im, cbar = heatmap(DFvalores, 
                        ListaLinhas, 
                        ListaColunas, 
                        ax=ax1,
                        cmap=mpl.colormaps["Wistia"].resampled(7), 
                        cbarlabel="QTD de Aceleração e Freadas Bruscas")
    texts = annotate_heatmap(im, valfmt="{x:.1f}", size=9, fontweight="bold", threshold=-1, textcolors=("red", "black"))
    fig1.tight_layout()               
    st.pyplot(fig1)

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current Axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

def Grafico_Pizza(Rotulos, Quantias, Legenda, posExplode, LocLEG, Larg = 16, Alt = 9, Titulo_Grafico = 'Título da Legenda', Titulo_legenda = 'Título da Legenda'):
    # Rotulos: etiquetamento dos dados
    # Quantias: dados numéricos referente a cada rótulo
    # Legenda: etiquetamento da legenda
    # posExplode: posição na qual se encontra a fatia da pizza que se deseja ressaltar (explodir)
    # LocLEG: Localização onde será posicionada a Legenda do Gráfico (Ref: https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/)

    #fig, ax = plt.subplots(figsize =(16, 9))
    fig, ax = plt.subplots(figsize =(Larg, Alt))
    explode = []
    for i in range(len(Rotulos)):
        if i !=posExplode:
            explode.append(0)
        else:
            explode.append(0.1)
    ax.pie(Quantias,
        explode=explode,
        labels=Legenda,
        autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title(Titulo_Grafico)
    
    ax.legend(title=Titulo_legenda,
            loc=LocLEG,
            bbox_to_anchor=(1, 0, 0.5, 1))
    #fig
    st.pyplot(fig)
 
def Ler_GooglePlanilha(url, coluna_indice = None):
    r = requests.get(url)
    dataD = r.content
    dfD = pd.read_csv(BytesIO(dataD), index_col=coluna_indice)   
    return dfD
    
def MKD(texto, alinhamento = "center", tamanho_fonte = 28, cor_fonte = "darkblue"):        
    conteudo = '<p style="font-weight: bolder; color:%s; font-size: %spx;">%s</p>'%(cor_fonte, tamanho_fonte, texto)    
    st.markdown(conteudo, unsafe_allow_html=True)
    mystyle0 = '''<style> p{text-align:%s;}</style>'''%(alinhamento)
    st.markdown(mystyle0, unsafe_allow_html=True) 

 
titulo  = "DashBUS 0.1"
Layout="wide"
barra_lateral = "auto"
ajuda = "https://docs.streamlit.io"
bug = "mailto:informacoes.actsp@gmail.com"
sobre="#### **ACT - Soluções para Pessoas**."
icone = "©️"
st.set_page_config(page_title=titulo, layout = Layout, initial_sidebar_state = barra_lateral, menu_items={'Get Help': (ajuda),
                                                                                                                            'Report a bug': (bug),
                                                                                                                            'About': (sobre)},page_icon=icone)
DadosOnline = False
                 
# Função para fazer o upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo XLSX", type="xlsx")

if uploaded_file is not None:
    # Leitura do arquivo XLSX em um DataFrame
    if not DadosOnline:
        df = pd.read_excel(uploaded_file)
    
    # Exibindo as três primeiras linhas do DataFrame
    #st.write("As três primeiras linhas do DataFrame são:")
    #st.write(df.head(3))   
        
    # TYP = Tipo
    # MOT = Motorista
    # MOT_USUAL = Motorista Usual
    # DATA = Data
    # VEIC = Veículo
    # I_VIAG = Início viagem
    # F_VIAG = Fim viagem
    # MOVIMTO = Movimto.
    # STOP = Parado
    # DUR = Duração viagem
    # DIST = Distancia
    # VEL_MX = Vel Max.
    # VEL_MD = Vel Med.
    # INT = Intervalo
    # LINE = Linha(s)
    # ECO_L = % Eco abaixo
    # ECO_D = % Eco dentro
    # ECO_H = % Eco acima
    # T_EXC_VEL = Tempo exc_Vel
    # T_EXC_rpm = Tempo exc_Rpm
    # PTO_MORTO = Ponto morto
    # ACEL_RAP = Aceler.rápida
    # FREA_B = Freada brusca
    # CURVA_A = Curva acent.
    # PTOS_DIR = Pontos Direção
    # PTOS_MOT = Pontos Motor
    # PTOS_T = Pontos Total
        
    df.columns = ['TYP', 'MOT', 'MOT_USUAL','DATA','VEIC','I_VIAG','F_VIAG','MOVMTO','STOP','DUR','DIST','VEL_MX','VEL_MD','INT','LINE','ECO_L','ECO_D','ECO_H','T_EXC_VEL','T_EXC_RPM','PTO_MORTO','ACEL_RAP','FREA_B','CURVA_A','PTOS_DIR','PTOS_MOT','PTOS_T']
    Colunas = ['TYP', 'MOT', 'MOT_USUAL','DATA','VEIC','I_VIAG','F_VIAG','MOVMTO','STOP','DUR','DIST','VEL_MX','VEL_MD','INT','LINE','ECO_L','ECO_D','ECO_H','T_EXC_VEL','T_EXC_RPM','PTO_MORTO','ACEL_RAP','FREA_B','CURVA_A','PTOS_DIR','PTOS_MOT','PTOS_T']
    for Coluna in Colunas:
        df[Coluna].fillna('', inplace=True) 
    
    #Rotina para corrigir erros na Formatação de data:
    df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
    df['DATA'] = pd.to_datetime(df['DATA'], format='%m/%d/%Y', errors='coerce')
    # Drop rows with invalid dates if any
    df.dropna(subset=['DATA'], inplace=True)
    # Format the column in 'dd/mm/yy' format
    df['DATA'] = df['DATA'].dt.strftime('%d/%m/%y')
        
    tab1, tab2, tab3 = st.tabs(["Base_Dados", "Dados_por_Motorista", "Dados_por_Motorista_e_Data"])

    with tab1:
        with st.expander("Clique para exibir Tabela de Dados GERAL"):
            st.write(df)
    
    Motoristas = df['MOT'].value_counts()
    #st.write(Motoristas.index)
    
    OPT = []
    for Filtro in Motoristas.index:
        OPT.append(Filtro)
    
    DataFiltro = st.text_input("Data: ", "20/06/24")   
    option = st.selectbox("Filtragem de Dados por Motorista:",OPT,index=0,placeholder="Selecione o nome do Motorista!")
    
    if option:
        selecao = df['MOT']==option
        df0 = df[selecao]
        with tab2:
            with st.expander("Clique para exibir Tabela de Dados"):
                st.write(df0)
        
        FiltraData = df0.loc[df0['DATA'] ==DataFiltro]
        ACEL_RAP_TOTAL = float(FiltraData['ACEL_RAP'].sum())
        ACEL_RAP_STD = float(FiltraData['ACEL_RAP'].std())
        FREA_B_TOTAL = float(FiltraData['FREA_B'].sum())
        FREA_B_STD = float(FiltraData['FREA_B'].std())
        CURVA_A_TOTAL = float(FiltraData['CURVA_A'].sum())
        CURVA_A_STD = float(FiltraData['CURVA_A'].std())        
        #Verificao do veículo que o Motorista selecionado mais dirige:
        VeiculosMOTselecionado = df0['VEIC'].value_counts()
        VEICULO_MAIS_DIRIGE = VeiculosMOTselecionado.index[0]
        
        #ROTINA PARA CÁLCULO DO TEMPO TOTAL EM MOVIMENTO DO VEÍCULO
        # Convertendo a coluna para o tipo timedelta
        FiltraData['MOVMTO'] = pd.to_timedelta(FiltraData['MOVMTO'])
        # Calculando a soma total dos tempos
        dfMOVMTO_limpo = FiltraData.dropna(subset=['MOVMTO'])
        TEMPO_TOTAL_MOVMTO = dfMOVMTO_limpo['MOVMTO'].sum()
        TEMPO_TOTAL_MOVMTO_min = TEMPO_TOTAL_MOVMTO.total_seconds() / 60

        #ROTINA PARA CÁLCULO DO TEMPO TOTAL VEÍCULO PARADO
        # Convertendo a coluna para o tipo timedelta
        FiltraData['STOP'] = pd.to_timedelta(FiltraData['STOP'])
        # Calculando a soma total dos tempos
        dfSTOP_limpo = FiltraData.dropna(subset=['STOP'])
        #st.write(dfSTOP_limpo)
        TEMPO_TOTAL_STOP = dfSTOP_limpo['STOP'].sum()
        TEMPO_TOTAL_STOP_min = TEMPO_TOTAL_STOP.total_seconds() / 60
        
        TemposMovSTOP = [TEMPO_TOTAL_MOVMTO_min, TEMPO_TOTAL_STOP_min]
        Rotulos_TemposMovSTOP = ['Em Movimento','Parado']
        
        with tab3:            
            with st.expander("Clique para exibir Tabela de Dados Filtrados por Motorista e Data"):
                st.write(FiltraData)
            
            st.divider()
            st.title("DashBUS - Painel para análise da Dirigibilidade Motoristas")
            ColsA = st.columns(4)
            with ColsA[0]:
                Container1 = st.container(border = True)
                with Container1:                     
                    ColsA1 = st.columns(2)
                    with ColsA1[0]: 
                        MKD('QTD de Acels. Rápidas', 'left', 28, 'black')
                    with ColsA1[1]:  
                        MKD(ACEL_RAP_TOTAL, 'left', 64, 'darkred')                        
                    MKD('O Desvio Padrão da Média é ' + str(round(ACEL_RAP_STD, 2)), 'left', 22, 'black')                        
            with ColsA[1]:
                Container2 = st.container(border = True)
                with Container2:                     
                    ColsA2 = st.columns(2)
                    with ColsA2[0]:
                        MKD('QTD de Freadas Bruscas', 'left', 28, 'black')                        
                    with ColsA2[1]:  
                        MKD(FREA_B_TOTAL, 'left', 64, 'red')                       
                    MKD('O Desvio Padrão da Média é ' + str(round(FREA_B_STD, 2)), 'left', 22, 'black')                     
            with ColsA[2]:           
                Container3 = st.container(border = True)
                with Container3:                     
                    ColsA3 = st.columns(2)
                    with ColsA3[0]:
                        MKD('QTD de Curvas Acentuadas', 'left', 28, 'black')                        
                    with ColsA3[1]:  
                        MKD(CURVA_A_TOTAL, 'left', 64, 'orange')                       
                    MKD('O Desvio Padrão da Média é ' + str(round(CURVA_A_STD, 2)), 'left', 22, 'black')            
            with ColsA[3]:
                Container4 = st.container(border = True)
                with Container4: 
                    #st.metric(label="Veículo Mais Dirige", value=str(VEICULO_MAIS_DIRIGE), delta='')
                    st.write('')
                    MKD('DADOS DOS VEÍCULOS UTILIZADOS', 'left', 22, 'black')
                    ColsA4 = st.columns(2)
                    with ColsA4[0]:
                        MKD('Veículo que mais Dirige ', 'left', 28, 'black')                        
                    with ColsA4[1]:  
                        MKD(VEICULO_MAIS_DIRIGE, 'left', 54, 'black')                       
                    st.write('') 
            ColsB = st.columns(3)
            with ColsB[0]:                                
                Container5 = st.container(border = True)
                with Container5:
                    st.write('')
                    st.write('')                    
                    MKD('TEMPO VEÍCULO EM MOVIMENTO', 'left', 22, 'blue')
                    ColsB1 = st.columns(2)
                    with ColsB1[0]:
                        MKD('Tempo Total Movimento', 'left', 28, 'black')                        
                    with ColsB1[1]:  
                        MKD(TEMPO_TOTAL_MOVMTO, 'left', 54, 'blue')    
                
                st.write('')
                Container6 = st.container(border = True)
                with Container6: 
                    MKD('TEMPO VEÍCULO PARADO', 'left', 22, 'orange')
                    ColsB2 = st.columns(2)
                    with ColsB2[0]:
                        MKD('Tempo Total Parado', 'left', 28, 'black')                        
                    with ColsB2[1]:  
                        MKD(TEMPO_TOTAL_STOP, 'left', 54, 'orange')         

            with ColsB[1]:
                Container7 = st.container(border = True)
                with Container7: 
                    n = len(OPT) 
                    mat = [[] for _ in range(n)]
                    for i in range(n):
                        for j in range(3):
                            valor = n  
                            if j==0:      
                                mat[i].append(OPT[i])  # Adiciona o valor à Coluna Nome
                                selecaoN = df['MOT']==OPT[i]
                                dfN = df[selecaoN]
                                FiltraDataN = dfN.loc[dfN['DATA'] ==DataFiltro]
                                ACEL_RAP_TOTAL = float(FiltraDataN['ACEL_RAP'].sum())
                                ACEL_RAP_STD = float(FiltraDataN['ACEL_RAP'].std())
                                FREA_B_TOTAL = float(FiltraDataN['FREA_B'].sum())
                                FREA_B_STD = float(FiltraDataN['FREA_B'].std())
                            elif j==1:      
                                mat[i].append(ACEL_RAP_TOTAL)  # Adiciona o valor à Coluna Dados1
                            if j==2:      
                                mat[i].append(FREA_B_TOTAL)  # Adiciona o valor à Coluna Dados2  
                    DFmat = pd.DataFrame(mat)
                    DFmat.columns = ['MOTORISTA', 'ACEL_RAP', 'FREA_B']
                    DFmat.set_index('MOTORISTA', inplace=True)
                    st.write('')
                    st.write('')
                    st.subheader('Tabela 01 - Total Aceleração e Freadas')
                    st.write(DFmat)
                    st.write('')
                    Grafico_Pizza(Rotulos_TemposMovSTOP, TemposMovSTOP, Rotulos_TemposMovSTOP, 0, "upper left", 4, 5, "Grafico 01 - Distribuição dos Tempos", "Tempos")
                 
            with ColsB[2]:
                #https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
                #https://matplotlib.org/stable/users/explain/colors/colormaps.html

                #Agora falta armazenar valores de aceleracao de cada motorista e depois colocar motoristas x Aceleração no HeatMap
                Container8 = st.container(border = True)
                with Container8:
                    st.write('')
                    st.write('')
                    st.subheader('Gráfico 01 - Dirigibilidade dos motoristas')
                    Colunas = ['Aceleração', 'Freadas_B']
                    Grafico_MapaCalor(DFmat, OPT, Colunas, 4, 5, 'Wistia')   
else:
    st.write("Por favor, faça o upload de um arquivo XLSX.")





