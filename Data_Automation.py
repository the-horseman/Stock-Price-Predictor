import Data.AXISBANK.AxisBank_Data_Collection as AxsBnk
import Data.BALKRISIND.Balkrishna_Data_Collection as BalKrish
import Data.BANKBARODA.BnkOfBaroda_Data_Collection as BnkBrda
import Data.BEL.Bel_Data_Collection as Bel
import Data.BHARTIARTL.BhrtiAirtl_Data_Collection as BhrtArtl
import Data.CANBK.CanraBnk_Data_Collection as CanBnk
import Data.EASEMYTRIP.EaseMyTrip_Data_Collection as EseMyTrp
import Data.GHCL.GHCL_Data_Collection as Ghcl
import Data.HDFCBANK.HDFC_Data_Collection as Hdfc
import Data.ICICIBANK.ICICI_Data_Collection as Icici
import Data.JUBLFOOD.Jubl_Food_Data_Collection as JblFood
import Data.KPITTECH.KPIT_Data_Collection as Kpit
import Data.LT.LNT_Data_Collection as Lnt
import Data.PRAJIND.PRAJ_Data_Collection as Praj
import Data.RELIANCE.Reliance_Data_Collection as Rel
import Data.TATAMOTORS.TataMot_Data_Collection as TatMotr
import Data.TATASTEEL.Tatasteel_Data_Collection as TatStl
import Data.TVSMOTOR.TVS_Data_Collection as TvsMtr
import Data.UPL.UPL_Data_Collection as Upl
import Data.WIPRO.Wipro_Data_Collection as Wpro

try:
    AxsBnk.axis_run()
except:
    AxsBnk.axis_run()
try:
    BalKrish.balkrish_run()
except:
    BalKrish.balkrish_run()
try:
    BnkBrda.broda_run()
except:
    BnkBrda.broda_run()
try:
    Bel.bel_run()
except:
    Bel.bel_run()
try:
    BhrtArtl.bhrtArtl_run()
except:
    BhrtArtl.bhrtArtl_run()
try:
    CanBnk.cnra_run()
except:
    CanBnk.cnra_run()
try:
    EseMyTrp.esemytrp_run()
except:
    EseMyTrp.esemytrp_run()
try:
    Ghcl.ghcl_run()
except:
    Ghcl.ghcl_run()
try:
    Hdfc.hdfc_run()
except:
    Hdfc.hdfc_run()
try:
    Icici.icici_run()
except:
    Icici.icici_run()
try:
    JblFood.jblfood_run()
except:
    JblFood.jblfood_run()
try:
    Kpit.kpit_run()
except:
    Kpit.kpit_run()
try:
    Lnt.lnt_run()
except:
    Lnt.lnt_run()
try:
    Praj.praj_run()
except:
    Praj.praj_run()
try:
    Rel.Rel_run()
except:
    Rel.Rel_run()
try:
    TatMotr.tatmotr_run()
except:
    TatMotr.tatmotr_run()
try:
    TatStl.tatstl_run()
except:
    TatStl.tatstl_run()
try:
    TvsMtr.tvsmotr_run()
except:
    TvsMtr.tvsmotr_run()
try:
    Upl.upl_run()
except:
    Upl.upl_run()
try:
    Wpro.wpro_run()
except:
    Wpro.wpro_run()

from git import Repo
from datetime import datetime
import os

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

Path_of_Repo = os.path.dirname(os.path.realpath(__file__)) + "/.git"
repo = Repo(Path_of_Repo)
repo.git.add(update=True)
repo.index.commit("Data Automation Commit for " + dt_string)
origin = repo.remote(name='origin')
origin.push()