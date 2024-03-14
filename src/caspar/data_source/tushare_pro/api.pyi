from .model import (
    TushareResponse as TushareResponse,
    TushareResponseError as TushareResponseError,
)
from datetime import datetime

class TushareProAPIBase:
    async def stock_basic(
        self,
        *,
        ts_code: str = None,
        name: str = None,
        market: str = None,
        list_status: str = None,
        exchange: str = None,
        is_hs: str = None,
    ) -> TushareResponse: ...
    async def trade_cal(
        self,
        *,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        is_open: str = None,
    ) -> TushareResponse: ...
    async def namechange(
        self, *, ts_code: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def hs_const(
        self, *, hs_type: str = None, is_new: str = None
    ) -> TushareResponse: ...
    async def stock_company(
        self, *, ts_code: str = None, exchange: str = None
    ) -> TushareResponse: ...
    async def stk_managers(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def stk_rewards(
        self, *, ts_code: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def new_share(
        self, *, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def bak_basic(
        self, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse: ...
    async def daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def weekly(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def monthly(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def adj_factor(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def realtime_quote(
        self, *, ts_code: str = None, src: str = None
    ) -> TushareResponse: ...
    async def realtime_tick(
        self, *, ts_code: str = None, src: str = None
    ) -> TushareResponse: ...
    async def realtime_list(self, *, src: str = None) -> TushareResponse: ...
    async def daily_basic(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def moneyflow(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def stk_limit(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def suspend_d(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        suspend_type: str = None,
    ) -> TushareResponse: ...
    async def moneyflow_hsgt(
        self, *, trade_date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def hsgt_top10(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        market_type: str = None,
    ) -> TushareResponse: ...
    async def ggt_top10(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        market_type: str = None,
    ) -> TushareResponse: ...
    async def ggt_daily(
        self, *, trade_date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def ggt_monthly(
        self, *, month: str = None, start_month: str = None, end_month: str = None
    ) -> TushareResponse: ...
    async def bak_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse: ...
    async def income(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        f_ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        report_type: str = None,
        comp_type: str = None,
    ) -> TushareResponse: ...
    async def balancesheet(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        report_type: str = None,
        comp_type: str = None,
    ) -> TushareResponse: ...
    async def cashflow(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        f_ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        report_type: str = None,
        comp_type: str = None,
        is_calc: int = None,
    ) -> TushareResponse: ...
    async def forecast(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        type: str = None,
    ) -> TushareResponse: ...
    async def express(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse: ...
    async def dividend(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        record_date: str = None,
        ex_date: str = None,
        imp_ann_date: str = None,
    ) -> TushareResponse: ...
    async def fina_indicator(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse: ...
    async def fina_audit(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse: ...
    async def fina_mainbz(
        self,
        *,
        ts_code: str = None,
        period: str = None,
        type: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def disclosure_date(
        self,
        *,
        ts_code: str = None,
        end_date: str = None,
        pre_date: str = None,
        actual_date: str = None,
    ) -> TushareResponse: ...
    async def margin(
        self,
        *,
        trade_date: str = None,
        exchange_id: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def margin_detail(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def margin_target(
        self, *, ts_code: str = None, is_new: str = None, mg_type: str = None
    ) -> TushareResponse: ...
    async def top10_holders(
        self,
        *,
        ts_code: str = None,
        period: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def top10_floatholders(
        self,
        *,
        ts_code: str = None,
        period: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def top_list(
        self, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse: ...
    async def top_inst(
        self, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse: ...
    async def pledge_stat(
        self, *, ts_code: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def pledge_detail(self, *, ts_code: str = None) -> TushareResponse: ...
    async def repurchase(
        self, *, ann_date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def concept(self, *, src: str = None) -> TushareResponse: ...
    async def concept_detail(
        self, *, id: str = None, ts_code: str = None
    ) -> TushareResponse: ...
    async def share_float(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        float_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def block_trade(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def stk_account(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def stk_account_old(
        self, *, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def stk_holdernumber(
        self,
        *,
        ts_code: str = None,
        enddate: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def stk_holdertrade(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        trade_type: str = None,
        holder_type: str = None,
    ) -> TushareResponse: ...
    async def report_rc(
        self,
        *,
        ts_code: str = None,
        report_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def cyq_perf(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def cyq_chips(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def stk_factor(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ccass_hold(
        self,
        *,
        ts_code: str = None,
        hk_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ccass_hold_detail(
        self,
        *,
        ts_code: str = None,
        hk_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def hk_hold(
        self,
        *,
        code: str = None,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def limit_list_d(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        limit_type: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ths_hot(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        hot_type: str = None,
        data_src: str = None,
        is_new: str = None,
    ) -> TushareResponse: ...
    async def stk_surv(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def broker_recommend(self, *, month: str = None) -> TushareResponse: ...
    async def hm_list(self, *, name: str = None) -> TushareResponse: ...
    async def hm_detail(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        hm_name: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_basic(
        self,
        *,
        ts_code: str = None,
        name: str = None,
        market: str = None,
        publisher: str = None,
        category: str = None,
    ) -> TushareResponse: ...
    async def index_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_weekly(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_monthly(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_weight(
        self,
        *,
        index_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: None = None,
    ) -> TushareResponse: ...
    async def index_dailybasic(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_classify(
        self,
        *,
        index_code: str = None,
        level: str = None,
        parent_code: str = None,
        src: str = None,
    ) -> TushareResponse: ...
    async def index_member(
        self, *, index_code: str = None, ts_code: str = None, is_new: str = None
    ) -> TushareResponse: ...
    async def daily_info(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def sz_daily_info(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ths_index(
        self, *, ts_code: str = None, exchange: str = None, type: str = None
    ) -> TushareResponse: ...
    async def ths_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ths_member(
        self, *, ts_code: str = None, code: str = None
    ) -> TushareResponse: ...
    async def ci_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def index_global(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fund_basic(
        self, *, ts_code: str = None, market: str = None, status: str = None
    ) -> TushareResponse: ...
    async def fund_company(
        self,
        *,
        name: str = None,
        shortname: str = None,
        short_enname: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
        phone: str = None,
        office: str = None,
        website: str = None,
        chairman: str = None,
        manager: str = None,
        reg_capital: float = None,
        setup_date: str = None,
        end_date: str = None,
        employees: float = None,
        main_business: str = None,
        org_code: str = None,
        credit_code: str = None,
    ) -> TushareResponse: ...
    async def fund_manager(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        name: str = None,
        offset: int = None,
        limit: int = None,
    ) -> TushareResponse: ...
    async def fund_share(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fund_nav(
        self,
        *,
        ts_code: str = None,
        nav_date: str = None,
        market: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fund_div(
        self,
        *,
        ann_date: str = None,
        ex_date: str = None,
        pay_date: str = None,
        ts_code: str = None,
    ) -> TushareResponse: ...
    async def fund_portfolio(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fund_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fund_adj(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse: ...
    async def fut_basic(
        self, *, exchange: str = None, fut_type: str = None, fut_code: str = None
    ) -> TushareResponse: ...
    async def trade_cal(
        self,
        *,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        is_open: int = None,
    ) -> TushareResponse: ...
    async def fut_daily(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ft_mins(
        self,
        *,
        ts_code: str = None,
        freq: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse: ...
    async def fut_wsr(
        self,
        *,
        trade_date: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def fut_settle(
        self,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def fut_holding(
        self,
        *,
        trade_date: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def index_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: None = None,
    ) -> TushareResponse: ...
    async def fut_mapping(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def fut_weekly_detail(
        self,
        *,
        week: str = None,
        prd: str = None,
        start_week: str = None,
        end_week: str = None,
        exchange: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def sge_basic(self, *, ts_code: str = None) -> TushareResponse: ...
    async def sge_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def opt_basic(
        self,
        *,
        ts_code: str = None,
        exchange: str = None,
        opt_code: str = None,
        call_put: str = None,
    ) -> TushareResponse: ...
    async def opt_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def cb_basic(
        self, *, ts_code: str = None, list_date: str = None, exchange: str = None
    ) -> TushareResponse: ...
    async def cb_issue(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def cb_call(self, *, ts_code: str = None) -> TushareResponse: ...
    async def cb_rate(self, *, ts_code: str = None) -> TushareResponse: ...
    async def cb_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def cb_price_chg(self, *, ts_code: str = None) -> TushareResponse: ...
    async def cb_share(self, *, ts_code: str = None) -> TushareResponse: ...
    async def repo_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def bond_blk(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def bond_blk_detail(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def yc_cb(
        self,
        *,
        ts_code: str = None,
        curve_type: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        curve_term: float = None,
    ) -> TushareResponse: ...
    async def eco_cal(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        currency: str = None,
        country: str = None,
        event: str = None,
    ) -> TushareResponse: ...
    async def fx_obasic(
        self, *, exchange: str = None, classify: str = None, ts_code: str = None
    ) -> TushareResponse: ...
    async def fx_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse: ...
    async def hk_basic(
        self, *, ts_code: str = None, list_status: str = None
    ) -> TushareResponse: ...
    async def hk_tradecal(
        self, *, start_date: str = None, end_date: str = None, is_open: str = None
    ) -> TushareResponse: ...
    async def hk_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def hk_mins(
        self,
        *,
        ts_code: str = None,
        freq: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse: ...
    async def us_basic(
        self,
        *,
        ts_code: str = None,
        classify: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse: ...
    async def us_tradecal(
        self, *, start_date: str = None, end_date: str = None, is_open: str = None
    ) -> TushareResponse: ...
    async def us_daily(
        self,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def tmt_twincome(
        self,
        *,
        date: str = None,
        item: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def tmt_twincomedetail(
        self,
        *,
        date: str = None,
        item: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        source: str = None,
    ) -> TushareResponse: ...
    async def bo_monthly(self, *, date: str = None) -> TushareResponse: ...
    async def bo_weekly(self, *, date: str = None) -> TushareResponse: ...
    async def bo_daily(self, *, date: str = None) -> TushareResponse: ...
    async def bo_cinema(self, *, date: str = None) -> TushareResponse: ...
    async def film_record(
        self, *, ann_date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def teleplay_record(
        self,
        *,
        report_date: str = None,
        start_date: str = None,
        end_date: str = None,
        org: str = None,
        name: str = None,
    ) -> TushareResponse: ...
    async def shibor(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def shibor_quote(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        bank: str = None,
    ) -> TushareResponse: ...
    async def shibor_lpr(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def libor(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        curr_type: str = None,
    ) -> TushareResponse: ...
    async def hibor(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def wz_index(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def gz_index(
        self, *, date: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def cn_gdp(
        self,
        *,
        q: str = None,
        start_q: str = None,
        end_q: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def cn_cpi(
        self, *, m: str = None, start_m: str = None, end_m: str = None
    ) -> TushareResponse: ...
    async def cn_ppi(
        self, *, m: str = None, start_m: str = None, end_m: str = None
    ) -> TushareResponse: ...
    async def cn_m(
        self,
        *,
        m: str = None,
        start_m: str = None,
        end_m: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def sf_month(
        self, *, m: str = None, start_m: str = None, end_m: str = None
    ) -> TushareResponse: ...
    async def us_tycr(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def us_trycr(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def us_tbr(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def us_tltr(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def us_trltr(
        self,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse: ...
    async def news(
        self, *, start_date: datetime = None, end_date: datetime = None, src: str = None
    ) -> TushareResponse: ...
    async def major_news(
        self, *, src: str = None, start_date: str = None, end_date: str = None
    ) -> TushareResponse: ...
    async def cctv_news(self, *, date: str = None) -> TushareResponse: ...
    async def anns_d(
        self,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ncov_num(
        self,
        *,
        area_name: str = None,
        level: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse: ...
    async def ncov_global(
        self,
        *,
        country: str = None,
        province: str = None,
        publish_date: datetime = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse: ...
    async def fund_sales_ratio(self, *, 年份: str = None) -> TushareResponse: ...
    async def fund_sales_vol(
        self, *, year: str = None, quarter: str = None, name: str = None
    ) -> TushareResponse: ...

class TushareProAPI(TushareProAPIBase):
    def __init__(
        self, token: str, *, base_url: str = "http://api.waditu.com", timeout: int = 30
    ) -> None: ...
    async def query(
        self, api_name: str, fields: str = "", **kwargs
    ) -> TushareResponse: ...
    def __getattribute__(self, item): ...
