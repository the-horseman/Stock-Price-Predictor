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

AxsBnk.axis_run()
BalKrish.balkrish_run()
BnkBrda.broda_run()
Bel.bel_run()
BhrtArtl.bhrtArtl_run()
CanBnk.cnra_run()
EseMyTrp.esemytrp_run()
Ghcl.ghcl_run()
Hdfc.hdfc_run()
Icici.icici_run()
JblFood.jblfood_run()
Kpit.kpit_run()
Lnt.lnt_run()
Praj.praj_run()
Rel.Rel_run()
TatMotr.tatmotr_run()
TatStl.tatstl_run()
TvsMtr.tvsmotr_run()
Upl.upl_run()
Wpro.wpro_run()

from git import Repo
from datetime import datetime
import os

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

Path_of_Repo = os.path.dirname(os.path.realpath(__file__)) + "/.git"
repo = Repo(Path_of_Repo)
repo.git.add(update=True)
repo.index.commit("Commit on " + dt_string)
origin = repo.remote(name='origin')
origin.push()