import streamlit as st
import random
def get_shuffled_deck(): #初始化洗好的牌
    suits={'♣', '♠', '♦', '♥'}
    ranks={'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck=[]
    #建立一副52張的撲克牌
    for suit in suits:
        for rank in ranks:
            deck.append(suit+' '+rank)
    random.shuffle(deck)
    return deck

#發一張牌給參與者participant
def deal_card(deck,participant):
    card=deck.pop()#取一張牌賦值給card，一般是最後一張
    participant.append(card)
    return card

#玩家拿牌： 詢問玩家是否繼續拿牌，如果是，繼續給玩家發牌(呼叫函式deal_ card()) ，並計算玩家牌點compute_total()，如果大於21點，輸出“玩家輸牌!”資訊，並返回。

#計算並返回一手牌的點數和
def compute_total(hand):
    values={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    result=0 #初始化點數為0
    for card in hand:
        result+=values[card[2:]]
    return result

def print_hand(hand):
    for card in hand:
       st.write(card,end=',')
    st.write()

def blackjack():
    deck=get_shuffled_deck()
    house=[]  #莊家的牌
    Player=[] #玩家的牌

    #依次給玩家和莊家各發兩張牌
    for i in range(2):
        deal_card(deck,Player)
        deal_card(deck,house)
    #列印一手牌
    st.write('莊家的牌：',end=' ');print_hand(house)
    st.write('玩家的牌：',end=' ');print_hand(Player)

    #詢問玩家是否繼續拿牌，如果是，繼續給玩家發牌
    answer=text_input('是否繼續拿牌（y/n,預設為y）:')
    while answer in('','y','Y'):
        card=deal_card(deck,Player)
        st.write('玩家拿到的牌為：',end='');print_hand(Player);
        #計算牌點
        if compute_total(Player)>21:
            st.write('爆掉，玩家輸了！')
            return
        answer=text_input('是否繼續拿牌（y/n,預設為y）:')

    #莊家（計算人工智慧）按“莊家規則”確定是否拿牌
    while compute_total(house)<17:
        card=deal_card(deck,house)
        st.write('莊家拿到的牌為：',end='');print_hand(house)
        #計算牌點
        if compute_total(house)>21:
            st.write('爆掉，莊家輸了！')
            return
    
    #分別計算莊家和玩家的點數，比較點數大小，輸出輸贏結果資訊
    houseTotal,playerTotal=compute_total(house),compute_total(Player)
    if houseTotal>=playerTotal:
        st.write('哭喔 輸了！')
    else:
        st.write('水喔 贏了！')

if __name__ == '__main__':
    blackjack()
