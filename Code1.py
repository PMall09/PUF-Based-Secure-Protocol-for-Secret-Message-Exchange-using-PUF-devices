usertype
Timestamp,Biometric,PUF,SK;
hashfunction H;
const XOR:Function;
const ADD:Function;
const MUL:Function;
const GEN:Function;
const BFIu,BFGu,Dc,Bc,T1,T2,IDc,Rc-as,Hc,Rc,T3,
T4,PWu,PWu',Ec,RANu,Ku,Lbs,T5,Rbs-u,RAN,CBc,
BIDr,IDu,Ras,Tbc,Obc,Nbc,Tbc,Tcb,Rbc,Sc,Rcb,
SKb-c,C1,XSs,ZSs,R1,SRs,SIDp,CIDq,SKe-v,SKbs-as;
const ADD:Function;
protocol SmartSociety(User, Cloud, BaseStation){
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
role User{
const IDu;#user identity
const PWu;#user password
const BFu;#biometric of the user
fresh Ras;
send_!4(User,Cloud,IDu);
macro BFu=H(BFIu,BFGu);
send_!5(User,Cloud,H(IDu, BFIu));
macro BFIu'=H(BFu,BFGu);
macro Dc'=H(XOR(IDu,PWu),BFIu');
match(Dc', Dc);
macro Ac'=XOR(Bc,H(IDu,H(IDu,BFIu)));
macro Fu=H(IDu,Ac',Ras,T1);
macro Ras-c=XOR (Ras ,H(Ac',T1));
macro Gu=H(IDu,Ac');
send_!6(User,Cloud,Fu,Ras-c,IDu,T1,Gu);
recv_!7(Cloud,User,Hc,Rc-as,IDc,T2);
macro Rc'=ADD(Ras,Ras-c);
macro Hc'=H(IDc,IDu,Ac',BFIu',Rc',T2);
match(Hc', Hc);
macro SKe-v = H(IDc,IDu,Ras,Rc );
claim_User(User,Niagree);#non-injective Agreement
claim_User(User, Nisynch);#non-injective Synchronization
claim_User(User,Secret,PWu);#verify the user password secrecy
claim_User(User,Secret, SKe-v);#verify the user and cloud server session key secrecy
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
role Cloud{
const Sc;
recv_!1(BaseStation,Cloud,BIDr);
const IDc;#cloud server identity
fresh Rc;#random number
macro BSr=H(BIDr,Sc);
send_!2(Cloud,BaseStation,BSr);
recv_!4(User,Cloud,IDu);
recv_!5(User,Cloud,H(IDu, BFIu));
macro Ac=H(H(IDu,BFIu),Sc);
macro Bc=XOR(Ac, H(IDu,H(IDu,BFIu)));
macro Dc=H(XOR(IDu,PWu),BFIu);
macro CBc=H(IDu,BIDr,BSr);
macro Ec=XOR(CBc,H(PWu,BFGu));
recv_!6(User,Cloud,Fu,Ras-c,IDu,T1,Gu);
macro Ac=H(H(IDu,BFIu),Sc);
macro Ras'=XOR(Ras-c, H(Ac,T1));
macro Fu'=H(IDu,Ac,Ras',T1);
match(Fu', Fu);
macro Hc=H(IDc,IDu,Ac,BFIu,Rc,T2);
macro Rc-as=XOR(Ras',Rc);
send_!7(Cloud,User,Hc,Rc-as,IDc,T2);
macro  SKe-v = H(IDc,IDu,Ras,Rc );
claim_Cloud(Cloud,Niagree);#non-injective Agreement
claim_Cloud(Cloud, Nisynch);#non-injective Synchronization
claim_Cloud(Cloud,Secret, SKe-v);#verify the user and cloud server session key secrecy

}
}
