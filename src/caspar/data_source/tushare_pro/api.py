from datetime import datetime
from functools import partial
from typing import Literal

from caspar.data_source.tushare_pro.model import TushareResponse, TushareResponseError
from caspar.data_source.model import DataSource


class TushareProAPIBase:
    def stock_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        name: str = None,
        market: Literal["主板", "创业板", "科创板", "CDR", "北交所"] = None,
        list_status: Literal["L", "D", "P"] = None,
        exchange: Literal["SSE", "SZSE", "BSE"] = None,
        is_hs: Literal["N", "H", "S"] = None,
    ) -> TushareResponse:
        """
        获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码. Defaults to None.
            name (str, optional): 名称. Defaults to None.
            market (Literal["主板", "创业板", "科创板", "CDR", "北交所"], optional): 市场类型 （主板/创业板/科创板/CDR/北交所）. Defaults to None.
            list_status (Literal["L", "D", "P"], optional): 上市状态 L上市 D退市 P暂停上市，默认是L. Defaults to None.
            exchange (Literal["SSE", "SZSE", "BSE"], optional): 交易所 SSE上交所 SZSE深交所 BSE北交所. Defaults to None.
            is_hs (Literal["N", "H", "S"], optional): 是否沪深港通标的，N否 H沪股通 S深股通. Defaults to None.
        """
        pass

    def trade_cal(
        self,
        _fields: list[str] = None,
        *,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        is_open: str = None,
    ) -> TushareResponse:
        """
        获取各大交易所交易日历数据,默认提取的是上交所

        Args:
            _fields (list[str], optional): Defaults to None.
            exchange (str, optional): 交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源. Defaults to None.
            start_date (str, optional): 开始日期 （格式：YYYYMMDD 下同）. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            is_open (str, optional): 是否交易 '0'休市 '1'交易. Defaults to None.
        """
        pass

    def namechange(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        历史名称变更记录

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def hs_const(
        self, _fields: list[str] = None, *, hs_type: str = None, is_new: str = None
    ) -> TushareResponse:
        """
        获取沪股通、深股通成分数据

        Args:
            _fields (list[str], optional): Defaults to None.
            hs_type (str, optional): 类型SH沪股通SZ深股通. Defaults to None.
            is_new (str, optional): 是否最新 1 是 0 否 (默认1). Defaults to None.
        """
        pass

    def stock_company(
        self, _fields: list[str] = None, *, ts_code: str = None, exchange: str = None
    ) -> TushareResponse:
        """
        获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            exchange (str, optional): 交易所代码 ，SSE上交所 SZSE深交所 BSE北交所. Defaults to None.
        """
        pass

    def stk_managers(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司管理层

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码，支持单个或多个股票输入. Defaults to None.
            ann_date (str, optional): 公告日期（YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def stk_rewards(
        self, _fields: list[str] = None, *, ts_code: str = None, end_date: str = None
    ) -> TushareResponse:
        """
        获取上市公司管理层薪酬和持股

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码，支持单个或多个代码输入. Defaults to None.
            end_date (str, optional): 报告期. Defaults to None.
        """
        pass

    def new_share(
        self, _fields: list[str] = None, *, start_date: str = None, end_date: str = None
    ) -> TushareResponse:
        """
        获取新股上市列表数据

        Args:
            _fields (list[str], optional): Defaults to None.
            start_date (str, optional): 上网发行开始日期. Defaults to None.
            end_date (str, optional): 上网发行结束日期. Defaults to None.
        """
        pass

    def bak_basic(
        self, _fields: list[str] = None, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse:
        """
        获取备用基础列表，数据从2016年开始

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
        """
        pass

    def daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取股票行情数据，或通过

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码（支持多个股票同时提取，逗号分隔）. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD）. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD). Defaults to None.
            end_date (str, optional): 结束日期(YYYYMMDD). Defaults to None.
        """
        pass

    def weekly(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取A股周线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码 （ts_code,trade_date两个参数任选一）. Defaults to None.
            trade_date (str, optional): 交易日期 （每周最后一个交易日期，YYYYMMDD格式）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def monthly(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取A股月线数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码 （ts_code,trade_date两个参数任选一）. Defaults to None.
            trade_date (str, optional): 交易日期 （每月最后一个交易日日期，YYYYMMDD格式）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def adj_factor(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取股票复权因子，可提取单只股票全部历史复权因子，也可以提取单日全部股票的复权因子。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def realtime_quote(
        self, _fields: list[str] = None, *, ts_code: str = None, src: str = None
    ) -> TushareResponse:
        """
        本接口是tushare org版实时接口的顺延，数据来自网络，且不进入tushare服务器，属于爬虫接口，请将tushare升级到1.3.3版本以上。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码，需按tushare. Defaults to None.
            src (str, optional): 代码输入，比如：000001.SZ表示平安银行，000001.SH表示上证指数. Defaults to None.
        """
        pass

    def realtime_tick(
        self, _fields: list[str] = None, *, ts_code: str = None, src: str = None
    ) -> TushareResponse:
        """
        本接口是tushare org版实时接口的顺延，数据来自网络，且不进入tushare服务器，属于爬虫接口，数据包括该股票当日开盘以来的所有分笔成交数据。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码，需按tushare. Defaults to None.
            src (str, optional): 输入，比如：000001.SZ表示平安银行，600000.SH表示浦发银行，单次只能输入一个股票. Defaults to None.
        """
        pass

    def realtime_list(
        self, _fields: list[str] = None, *, src: str = None
    ) -> TushareResponse:
        """
        本接口是tushare org版实时接口的顺延，数据来自网络，且不进入tushare服务器，属于爬虫接口，数据包括该股票当日开盘以来的所有分笔成交数据。

        Args:
            _fields (list[str], optional): Defaults to None.
            src (str, optional): 数据源 （sina-新浪 dc-东方财富，默认dc）. Defaults to None.
        """
        pass

    def daily_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码（二选一）. Defaults to None.
            trade_date (str, optional): 交易日期 （二选一）. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD). Defaults to None.
            end_date (str, optional): 结束日期(YYYYMMDD). Defaults to None.
        """
        pass

    def moneyflow(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向，数据开始于2010年。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码 （股票和时间参数至少输入一个）. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def stk_limit(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取全市场（包含A/B股和基金）每日涨跌停价格，包括涨停价格，跌停价格等，每个交易日8点40左右更新当日股票涨跌停价格。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def suspend_d(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        suspend_type: str = None,
    ) -> TushareResponse:
        """
        按日期方式获取股票每日停复牌信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码(可输入多值). Defaults to None.
            trade_date (str, optional): 交易日日期. Defaults to None.
            start_date (str, optional): 停复牌查询开始日期. Defaults to None.
            end_date (str, optional): 停复牌查询结束日期. Defaults to None.
            suspend_type (str, optional): 停复牌类型：S-停牌,R-复牌. Defaults to None.
        """
        pass

    def moneyflow_hsgt(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪股通、深股通、港股通每日资金流向数据，每次最多返回300条记录，总量不限制。每天18~20点之间完成当日更新

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期 (二选一). Defaults to None.
            start_date (str, optional): 开始日期 (二选一). Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def hsgt_top10(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        market_type: str = None,
    ) -> TushareResponse:
        """
        获取沪股通、深股通每日前十大成交详细数据，每天18~20点之间完成当日更新

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码（二选一）. Defaults to None.
            trade_date (str, optional): 交易日期（二选一）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            market_type (str, optional): 市场类型（1：沪市 3：深市）. Defaults to None.
        """
        pass

    def ggt_top10(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        market_type: str = None,
    ) -> TushareResponse:
        """
        获取港股通每日成交数据，其中包括沪市、深市详细数据，每天18~20点之间完成当日更新

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码（二选一）. Defaults to None.
            trade_date (str, optional): 交易日期（二选一）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            market_type (str, optional): 市场类型 2：港股通（沪） 4：港股通（深）. Defaults to None.
        """
        pass

    def ggt_daily(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取港股通每日成交信息，数据从2014年开始

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期 （格式YYYYMMDD，下同。支持单日和多日输入）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ggt_monthly(
        self,
        _fields: list[str] = None,
        *,
        month: str = None,
        start_month: str = None,
        end_month: str = None,
    ) -> TushareResponse:
        """
        港股通每月成交信息，数据从2014年开始

        Args:
            _fields (list[str], optional): Defaults to None.
            month (str, optional): 月度（格式YYYYMM，下同，支持多个输入）. Defaults to None.
            start_month (str, optional): 开始月度. Defaults to None.
            end_month (str, optional): 结束月度. Defaults to None.
        """
        pass

    def bak_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse:
        """
        获取备用行情，包括特定的行情指标(数据从2017年中左右开始，早期有几天数据缺失，近期正常)

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            offset (str, optional): 开始行数. Defaults to None.
            limit (str, optional): 最大行数. Defaults to None.
        """
        pass

    def income(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        f_ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        report_type: str = None,
        comp_type: str = None,
    ) -> TushareResponse:
        """
        获取上市公司财务利润表数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期（YYYYMMDD格式，下同）. Defaults to None.
            f_ann_date (str, optional): 实际公告日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期，比如20171231表示年报). Defaults to None.
            report_type (str, optional): 报告类型. Defaults to None.
            comp_type (str, optional): 公司类型（1一般工商业2银行3保险4证券）. Defaults to None.
        """
        pass

    def balancesheet(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        report_type: str = None,
        comp_type: str = None,
    ) -> TushareResponse:
        """
        获取上市公司资产负债表

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期，比如20171231表示年报). Defaults to None.
            report_type (str, optional): 报告类型：见下方详细说明. Defaults to None.
            comp_type (str, optional): 公司类型：1一般工商业 2银行 3保险 4证券. Defaults to None.
        """
        pass

    def cashflow(
        self,
        _fields: list[str] = None,
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
    ) -> TushareResponse:
        """
        获取上市公司现金流量表

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期（YYYYMMDD格式，下同）. Defaults to None.
            f_ann_date (str, optional): 实际公告日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期，比如20171231表示年报). Defaults to None.
            report_type (str, optional): 报告类型：见下方详细说明. Defaults to None.
            comp_type (str, optional): 公司类型：1一般工商业 2银行 3保险 4证券. Defaults to None.
            is_calc (int, optional): 是否计算报表. Defaults to None.
        """
        pass

    def forecast(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        type: str = None,
    ) -> TushareResponse:
        """
        获取业绩预告数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码(二选一). Defaults to None.
            ann_date (str, optional): 公告日期 (二选一). Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期，比如20171231表示年报). Defaults to None.
            type (str, optional): 预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减). Defaults to None.
        """
        pass

    def express(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse:
        """
        获取上市公司业绩快报

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期,比如20171231表示年报). Defaults to None.
        """
        pass

    def dividend(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        record_date: str = None,
        ex_date: str = None,
        imp_ann_date: str = None,
    ) -> TushareResponse:
        """
        分红送股数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            ann_date (str, optional): 公告日. Defaults to None.
            record_date (str, optional): 股权登记日期. Defaults to None.
            ex_date (str, optional): 除权除息日. Defaults to None.
            imp_ann_date (str, optional): 实施公告日. Defaults to None.
        """
        pass

    def fina_indicator(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse:
        """
        获取上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回60条记录，可通过设置日期多次请求获取更多数据。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码,e.g. 600001.SH/000001.SZ. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期,比如20171231表示年报). Defaults to None.
        """
        pass

    def fina_audit(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        period: str = None,
    ) -> TushareResponse:
        """
        获取上市公司定期财务审计意见数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期,比如20171231表示年报). Defaults to None.
        """
        pass

    def fina_mainbz(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        period: str = None,
        type: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获得上市公司主营业务构成，分地区和产品两种方式

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            period (str, optional): 报告期(每个季度最后一天的日期,比如20171231表示年报). Defaults to None.
            type (str, optional): 类型：P按产品 D按地区 I按行业（请输入大写字母P或者D）. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
        """
        pass

    def disclosure_date(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        end_date: str = None,
        pre_date: str = None,
        actual_date: str = None,
    ) -> TushareResponse:
        """
        获取财报披露计划日期

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码. Defaults to None.
            end_date (str, optional): 财报周期（比如20181231表示2018年年报，20180630表示中报）. Defaults to None.
            pre_date (str, optional): 计划披露日期. Defaults to None.
            actual_date (str, optional): 实际披露日期. Defaults to None.
        """
        pass

    def margin(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        exchange_id: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取融资融券每日交易汇总数据

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            exchange_id (str, optional): 交易所代码（SSE上交所SZSE深交所BSE北交所）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def margin_detail(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪深两市每日融资融券明细

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def margin_target(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        is_new: str = None,
        mg_type: str = None,
    ) -> TushareResponse:
        """
        获取全市场融资融券标的

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            is_new (str, optional): 是否最新. Defaults to None.
            mg_type (str, optional): 标的类型：B买入标的 S卖出标的. Defaults to None.
        """
        pass

    def top10_holders(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        period: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司前十大股东数据，包括持有数量和比例等信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            period (str, optional): 报告期（YYYYMMDD格式，一般为每个季度最后一天）. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
        """
        pass

    def top10_floatholders(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        period: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司前十大流通股东数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            period (str, optional): 报告期（YYYYMMDD格式，一般为每个季度最后一天）. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
        """
        pass

    def top_list(
        self, _fields: list[str] = None, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse:
        """
        龙虎榜每日交易明细

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
        """
        pass

    def top_inst(
        self, _fields: list[str] = None, *, trade_date: str = None, ts_code: str = None
    ) -> TushareResponse:
        """
        龙虎榜机构成交明细

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
        """
        pass

    def pledge_stat(
        self, _fields: list[str] = None, *, ts_code: str = None, end_date: str = None
    ) -> TushareResponse:
        """
        获取股票质押统计数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            end_date (str, optional): 截止日期. Defaults to None.
        """
        pass

    def pledge_detail(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取股票质押明细数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
        """
        pass

    def repurchase(
        self,
        _fields: list[str] = None,
        *,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司回购股票数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ann_date (str, optional): 公告日期（任意填参数，如果都不填，单次默认返回2000条）. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def concept(self, _fields: list[str] = None, *, src: str = None) -> TushareResponse:
        """
        获取概念股分类，目前只有ts一个来源，未来将逐步增加来源

        Args:
            _fields (list[str], optional): Defaults to None.
            src (str, optional): 来源，默认为ts. Defaults to None.
        """
        pass

    def concept_detail(
        self, _fields: list[str] = None, *, id: str = None, ts_code: str = None
    ) -> TushareResponse:
        """
        获取概念股分类明细数据

        Args:
            _fields (list[str], optional): Defaults to None.
            id (str, optional): 概念分类ID （id来自概念股分类接口）. Defaults to None.
            ts_code (str, optional): 股票代码  （以上参数二选一）. Defaults to None.
        """
        pass

    def share_float(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        float_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取限售股解禁

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码（至少输入一个参数）. Defaults to None.
            ann_date (str, optional): 公告日期（日期格式：YYYYMMDD，下同）. Defaults to None.
            float_date (str, optional): 解禁日期. Defaults to None.
            start_date (str, optional): 解禁开始日期. Defaults to None.
            end_date (str, optional): 解禁结束日期. Defaults to None.
        """
        pass

    def block_trade(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        大宗交易

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码（股票代码和日期至少输入一个参数）. Defaults to None.
            trade_date (str, optional): 交易日期（格式：YYYYMMDD，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def stk_account(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取股票账户开户数据，统计周期为一周

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def stk_account_old(
        self, _fields: list[str] = None, *, start_date: str = None, end_date: str = None
    ) -> TushareResponse:
        """
        获取股票账户开户数据旧版格式数据，数据从2008年1月开始，到2015年5月29，新数据请通过

        Args:
            _fields (list[str], optional): Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def stk_holdernumber(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        enddate: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司股东户数数据，数据不定期公布

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码. Defaults to None.
            enddate (str, optional): 截止日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def stk_holdertrade(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
        trade_type: str = None,
        holder_type: str = None,
    ) -> TushareResponse:
        """
        获取上市公司增减持数据，了解重要股东近期及历史上的股份增减变化

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS股票代码. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
            trade_type (str, optional): 交易类型IN增持DE减持. Defaults to None.
            holder_type (str, optional): 股东类型C公司P个人G高管. Defaults to None.
        """
        pass

    def report_rc(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        report_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取券商（卖方）每天研报的盈利预测数据，数据从2010年开始，每晚19~22点更新当日数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            report_date (str, optional): 报告日期. Defaults to None.
            start_date (str, optional): 报告开始日期. Defaults to None.
            end_date (str, optional): 报告结束日期. Defaults to None.
        """
        pass

    def cyq_perf(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取A股每日筹码平均成本和胜率情况，每天17~18点左右更新，数据从2005年开始

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def cyq_chips(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取A股每日的筹码分布情况，提供各价位占比，数据从2010年开始，每天17~18点之间更新当日数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def stk_factor(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取股票每日技术面因子数据，用于跟踪股票当前走势情况，数据由Tushare社区自产，覆盖全历史

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期 （yyyymmdd，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ccass_hold(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        hk_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取中央结算系统持股汇总数据，覆盖全部历史数据，根据交易所披露时间，当日数据在下一交易日早上9点前完成入库

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码 (e.g. 605009.SH). Defaults to None.
            hk_code (str, optional): 港交所代码 （e.g. 95009）. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ccass_hold_detail(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        hk_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取中央结算系统机构席位持股明细，数据覆盖

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码 (e.g. 605009.SH). Defaults to None.
            hk_code (str, optional): 港交所代码 （e.g. 95009）. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def hk_hold(
        self,
        _fields: list[str] = None,
        *,
        code: str = None,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取沪深港股通持股明细，数据来源港交所。

        Args:
            _fields (list[str], optional): Defaults to None.
            code (str, optional): 交易所代码. Defaults to None.
            ts_code (str, optional): TS股票代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            exchange (str, optional): 类型：SH沪股通（北向）SZ深股通（北向）HK港股通（南向持股）. Defaults to None.
        """
        pass

    def limit_list_d(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        limit_type: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪深A股每日涨跌停、炸板数据情况，数据从2020年开始

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            limit_type (str, optional): 涨跌停类型（U涨停D跌停Z炸板）. Defaults to None.
            exchange (str, optional): 交易所（SH上交所SZ深交所BJ北交所）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ths_hot(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        hot_type: str = None,
        data_src: str = None,
        is_new: str = None,
    ) -> TushareResponse:
        """
        获取同花顺App热榜数据，包括热股、概念板块、ETF、可转债、港美股等等

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            hot_type (str, optional): 热板类型(热股、ETF、可转债、行业板块、概念板块、期货、港股、热基、美股). Defaults to None.
            data_src (str, optional): 数据源. Defaults to None.
            is_new (str, optional): 是否最新. Defaults to None.
        """
        pass

    def stk_surv(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上市公司机构调研记录数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 调研日期. Defaults to None.
            start_date (str, optional): 调研开始日期. Defaults to None.
            end_date (str, optional): 调研结束日期. Defaults to None.
        """
        pass

    def broker_recommend(
        self, _fields: list[str] = None, *, month: str = None
    ) -> TushareResponse:
        """
        获取券商月度金股，一般1日~3日内更新当月数据

        Args:
            _fields (list[str], optional): Defaults to None.
            month (str, optional): 月度（YYYYMM）. Defaults to None.
        """
        pass

    def hm_list(
        self, _fields: list[str] = None, *, name: str = None
    ) -> TushareResponse:
        """
        获取游资分类名录信息

        Args:
            _fields (list[str], optional): Defaults to None.
            name (str, optional): 游资名称. Defaults to None.
        """
        pass

    def hm_detail(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        hm_name: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取每日游资交易明细，数据开始于2022年8。游资分类名录，请点击

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD). Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            hm_name (str, optional): 游资名称. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD). Defaults to None.
            end_date (str, optional): 结束日期(YYYYMMDD). Defaults to None.
        """
        pass

    def index_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        name: str = None,
        market: str = None,
        publisher: str = None,
        category: str = None,
    ) -> TushareResponse:
        """
        获取指数基础信息。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 指数代码. Defaults to None.
            name (str, optional): 指数简称. Defaults to None.
            market (str, optional): 交易所或服务商(默认SSE). Defaults to None.
            publisher (str, optional): 发布商. Defaults to None.
            category (str, optional): 指数类别. Defaults to None.
        """
        pass

    def index_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取指数每日行情，还可以通过bar接口获取。由于服务器压力，目前规则是单次调取最多取8000行记录，可以设置start和end日期补全。指数行情也可以通过

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 指数代码. Defaults to None.
            trade_date (str, optional): 交易日期 （日期格式：YYYYMMDD，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def index_weekly(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取指数周线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def index_monthly(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取指数月线行情,每月更新一次

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def index_weight(
        self,
        _fields: list[str] = None,
        *,
        index_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: None = None,
    ) -> TushareResponse:
        """
        获取各类指数成分和权重，

        Args:
            _fields (list[str], optional): Defaults to None.
            index_code (str, optional): 指数代码 (二选一). Defaults to None.
            trade_date (str, optional): 交易日期 （二选一）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (None, optional): 结束日期. Defaults to None.
        """
        pass

    def index_dailybasic(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        目前只提供上证综指，深证成指，上证50，中证500，中小板指，创业板指的每日指标数据

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期 （格式：YYYYMMDD，比如20181018，下同）. Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def index_classify(
        self,
        _fields: list[str] = None,
        *,
        index_code: str = None,
        level: str = None,
        parent_code: str = None,
        src: str = None,
    ) -> TushareResponse:
        """
        获取申万行业分类，可以获取申万2014年版本（28个一级分类，104个二级分类，227个三级分类）和2021年本版（31个一级分类，134个二级分类，346个三级分类）列表信息

        Args:
            _fields (list[str], optional): Defaults to None.
            index_code (str, optional): 指数代码. Defaults to None.
            level (str, optional): 行业级别（L1/L2/L3）. Defaults to None.
            parent_code (str, optional): 父级代码（一级为0）. Defaults to None.
            src (str, optional): 指数来源（SW2014：申万2014年版本，SW2021：申万2021年版本）. Defaults to None.
        """
        pass

    def index_member(
        self,
        _fields: list[str] = None,
        *,
        index_code: str = None,
        ts_code: str = None,
        is_new: str = None,
    ) -> TushareResponse:
        """
        申万行业成分

        Args:
            _fields (list[str], optional): Defaults to None.
            index_code (str, optional): 指数代码. Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            is_new (str, optional): 是否最新（默认为“Y是”）. Defaults to None.
        """
        pass

    def daily_info(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取交易所股票交易统计，包括各板块明细

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            ts_code (str, optional): 板块代码（请参阅下方列表）. Defaults to None.
            exchange (str, optional): 股票市场（SH上交所 SZ深交所）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定提取字段. Defaults to None.
        """
        pass

    def sz_daily_info(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取深圳市场每日交易概况

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            ts_code (str, optional): 板块代码. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ths_index(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        exchange: str = None,
        type: str = None,
    ) -> TushareResponse:
        """
        获取同花顺板块指数。注：数据版权归属同花顺，如做商业用途，请主动联系同花顺，如需帮助请联系微信migedata 。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 指数代码. Defaults to None.
            exchange (str, optional): 市场类型A-a股 HK-港股 US-美股. Defaults to None.
            type (str, optional): 指数类型 N-概念指数 I-行业指数 R-地域指数 S-同花顺特色指数 ST-同花顺风格指数 TH-同花顺主题指数 BB-同花顺宽基指数. Defaults to None.
        """
        pass

    def ths_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取同花顺板块指数行情。注：数据版权归属同花顺，如做商业用途，请主动联系同花顺，如需帮助请联系微信migedata 。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 指数代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ths_member(
        self, _fields: list[str] = None, *, ts_code: str = None, code: str = None
    ) -> TushareResponse:
        """
        获取同花顺概念板块成分列表注：数据版权归属同花顺，如做商业用途，请主动联系同花顺。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 板块指数代码. Defaults to None.
            code (str, optional): 股票代码. Defaults to None.
        """
        pass

    def ci_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取中信行业指数日线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 行业代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def index_global(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取国际主要指数日线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS指数代码，见下表. Defaults to None.
            trade_date (str, optional): 交易日期，YYYYMMDD格式，下同. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def fund_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        market: str = None,
        status: str = None,
    ) -> TushareResponse:
        """
        获取公募基金数据列表，包括场内和场外基金

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 基金代码. Defaults to None.
            market (str, optional): 交易市场: E场内 O场外（默认E）. Defaults to None.
            status (str, optional): 存续状态 D摘牌 I发行 L上市中. Defaults to None.
        """
        pass

    def fund_company(
        self,
        _fields: list[str] = None,
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
    ) -> TushareResponse:
        """
        获取公募基金管理人列表

        Args:
            _fields (list[str], optional): Defaults to None.
            name (str, optional): 基金公司名称. Defaults to None.
            shortname (str, optional): 简称. Defaults to None.
            short_enname (str, optional): 英文缩写. Defaults to None.
            province (str, optional): 省份. Defaults to None.
            city (str, optional): 城市. Defaults to None.
            address (str, optional): 注册地址. Defaults to None.
            phone (str, optional): 电话. Defaults to None.
            office (str, optional): 办公地址. Defaults to None.
            website (str, optional): 公司网址. Defaults to None.
            chairman (str, optional): 法人代表. Defaults to None.
            manager (str, optional): 总经理. Defaults to None.
            reg_capital (float, optional): 注册资本. Defaults to None.
            setup_date (str, optional): 成立日期. Defaults to None.
            end_date (str, optional): 公司终止日期. Defaults to None.
            employees (float, optional): 员工总数. Defaults to None.
            main_business (str, optional): 主要产品及业务. Defaults to None.
            org_code (str, optional): 组织机构代码. Defaults to None.
            credit_code (str, optional): 统一社会信用代码. Defaults to None.
        """
        pass

    def fund_manager(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        name: str = None,
        offset: int = None,
        limit: int = None,
    ) -> TushareResponse:
        """
        获取公募基金经理数据，包括基金经理简历等数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 基金代码，支持多只基金，逗号分隔. Defaults to None.
            ann_date (str, optional): 公告日期，格式：YYYYMMDD. Defaults to None.
            name (str, optional): 基金经理姓名. Defaults to None.
            offset (int, optional): 开始行数. Defaults to None.
            limit (int, optional): 每页行数. Defaults to None.
        """
        pass

    def fund_share(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取基金规模数据，包含上海和深圳ETF基金

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS基金代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def fund_nav(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        nav_date: str = None,
        market: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取公募基金净值数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS基金代码 （二选一）. Defaults to None.
            nav_date (str, optional): 净值日期 （二选一）. Defaults to None.
            market (str, optional): E场内 O场外. Defaults to None.
            start_date (str, optional): 净值开始日期. Defaults to None.
            end_date (str, optional): 净值结束日期. Defaults to None.
        """
        pass

    def fund_div(
        self,
        _fields: list[str] = None,
        *,
        ann_date: str = None,
        ex_date: str = None,
        pay_date: str = None,
        ts_code: str = None,
    ) -> TushareResponse:
        """
        获取公募基金分红数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ann_date (str, optional): 公告日（以下参数四选一）. Defaults to None.
            ex_date (str, optional): 除息日. Defaults to None.
            pay_date (str, optional): 派息日. Defaults to None.
            ts_code (str, optional): 基金代码. Defaults to None.
        """
        pass

    def fund_portfolio(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取公募基金持仓数据，季度更新

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 基金代码. Defaults to None.
            ann_date (str, optional): 公告日期（YYYYMMDD格式）. Defaults to None.
            start_date (str, optional): 报告期开始日期（YYYYMMDD格式）. Defaults to None.
            end_date (str, optional): 报告期结束日期（YYYYMMDD格式）. Defaults to None.
        """
        pass

    def fund_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取场内基金日线行情，类似股票日行情，包括ETF行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 基金代码. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def fund_adj(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse:
        """
        获取基金复权因子，用于计算基金复权行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS基金代码（支持多只基金输入）. Defaults to None.
            trade_date (str, optional): 交易日期（格式：yyyymmdd，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            offset (str, optional): 开始行数. Defaults to None.
            limit (str, optional): 最大行数. Defaults to None.
        """
        pass

    def fut_basic(
        self,
        _fields: list[str] = None,
        *,
        exchange: str = None,
        fut_type: str = None,
        fut_code: str = None,
    ) -> TushareResponse:
        """
        获取期货合约列表数据

        Args:
            _fields (list[str], optional): Defaults to None.
            exchange (str, optional): 交易所代码 CFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心 GFEX-广州期货交易所. Defaults to None.
            fut_type (str, optional): 合约类型 (1 普通合约 2主力与连续合约 默认取全部). Defaults to None.
            fut_code (str, optional): 标准合约代码，如白银AG、AP鲜苹果等. Defaults to None.
        """
        pass

    def trade_cal(
        self,
        _fields: list[str] = None,
        *,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
        is_open: int = None,
    ) -> TushareResponse:
        """
        获取各大期货交易所交易日历数据

        Args:
            _fields (list[str], optional): Defaults to None.
            exchange (str, optional): 交易所 SHFE 上期所 DCE 大商所 CFFEX中金所  CZCE郑商所 INE上海国际能源交易所. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            is_open (int, optional): 是否交易 0休市 1交易. Defaults to None.
        """
        pass

    def fut_daily(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        exchange: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        期货日线行情数据

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            ts_code (str, optional): 合约代码. Defaults to None.
            exchange (str, optional): 交易所代码. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def ft_mins(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        freq: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse:
        """
        获取全市场期货合约分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式，如果需要主力合约分钟，请先通过主力

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码，e.g.CU2310.SHF. Defaults to None.
            freq (str, optional): 分钟频度（1min/5min/15min/30min/60min）. Defaults to None.
            start_date (datetime, optional): 开始日期 格式：2023-08-25 09:00:00. Defaults to None.
            end_date (datetime, optional): 结束时间 格式：2023-08-25 19:00:00. Defaults to None.
        """
        pass

    def fut_wsr(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取仓单日报数据，了解各仓库/厂库的仓单变化

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            symbol (str, optional): 产品代码. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD格式，下同). Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            exchange (str, optional): 交易所代码. Defaults to None.
        """
        pass

    def fut_settle(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        ts_code: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取每日结算参数数据，包括交易和交割费率等

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期 （trade_date/ts_code至少需要输入一个参数）. Defaults to None.
            ts_code (str, optional): 合约代码. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD格式，下同). Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            exchange (str, optional): 交易所代码. Defaults to None.
        """
        pass

    def fut_holding(
        self,
        _fields: list[str] = None,
        *,
        trade_date: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取每日成交持仓排名数据

        Args:
            _fields (list[str], optional): Defaults to None.
            trade_date (str, optional): 交易日期 （trade_date/symbol至少输入一个参数）. Defaults to None.
            symbol (str, optional): 合约或产品代码. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD格式，下同). Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            exchange (str, optional): 交易所代码. Defaults to None.
        """
        pass

    def index_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: None = None,
    ) -> TushareResponse:
        """
        获取南华指数每日行情，指数行情也可以通过

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 指数代码（南华期货指数以 .NH 结尾，具体请参考本文最下方）. Defaults to None.
            trade_date (str, optional): 交易日期 （日期格式：YYYYMMDD，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (None, optional): 结束日期. Defaults to None.
        """
        pass

    def fut_mapping(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取期货主力（或连续）合约与月合约映射数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 合约代码. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def fut_weekly_detail(
        self,
        _fields: list[str] = None,
        *,
        week: str = None,
        prd: str = None,
        start_week: str = None,
        end_week: str = None,
        exchange: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取期货交易所主要品种每周交易统计信息，数据从2010年3月开始

        Args:
            _fields (list[str], optional): Defaults to None.
            week (str, optional): 周期（每年第几周，e.g. 202001 表示2020第1周）. Defaults to None.
            prd (str, optional): 期货品种（支持多品种输入，逗号分隔）. Defaults to None.
            start_week (str, optional): 开始周期. Defaults to None.
            end_week (str, optional): 结束周期. Defaults to None.
            exchange (str, optional): 交易所（请参考. Defaults to None.
            fields (str, optional): ）. Defaults to None.
        """
        pass

    def sge_basic(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取上海黄金交易所现货合约基础信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 合约代码 （支持多个，逗号分隔，不输入为获取全部）. Defaults to None.
        """
        pass

    def sge_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取上海黄金交易所现货合约日线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 合约代码，可通过. Defaults to None.
            trade_date (str, optional): 获得. Defaults to None.
            start_date (str, optional): 交易日期. Defaults to None.
            end_date (str, optional): 开始日期. Defaults to None.
        """
        pass

    def opt_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        exchange: str = None,
        opt_code: str = None,
        call_put: str = None,
    ) -> TushareResponse:
        """
        获取期权合约信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS期权代码. Defaults to None.
            exchange (str, optional): 交易所代码 （包括上交所SSE等. Defaults to None.
            opt_code (str, optional): ）. Defaults to None.
            call_put (str, optional): 标准合约代码，OP+期货合约TS_CODE，如棕榈油2207合约，输入OPP2207.DCE. Defaults to None.
        """
        pass

    def opt_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取期权日线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS合约代码（输入代码或时间至少任意一个参数）. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            exchange (str, optional): 交易所（SSE/SZSE/CFFEX/DCE/SHFE/CZCE）. Defaults to None.
        """
        pass

    def cb_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        list_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取可转债基本信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 转债代码. Defaults to None.
            list_date (str, optional): 上市日期. Defaults to None.
            exchange (str, optional): 上市地点. Defaults to None.
        """
        pass

    def cb_issue(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取可转债发行数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            ann_date (str, optional): 发行公告日. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def cb_call(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取可转债到期赎回、强制赎回等信息。数据来源于公开披露渠道，供个人和机构研究使用，请不要用于数据商业目的。

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 转债代码，支持多值输入. Defaults to None.
        """
        pass

    def cb_rate(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取可转债票面利率

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 转债代码，支持多值输入. Defaults to None.
        """
        pass

    def cb_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取可转债行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def cb_price_chg(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取可转债转股价变动

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 转债代码，支持多值输入. Defaults to None.
        """
        pass

    def cb_share(
        self, _fields: list[str] = None, *, ts_code: str = None
    ) -> TushareResponse:
        """
        获取可转债转股结果

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 转债代码，支持多值输入. Defaults to None.
        """
        pass

    def repo_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        债券回购日行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            trade_date (str, optional): 交易日期(YYYYMMDD格式，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def bond_blk(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪深交易所债券大宗交易数据，可以通过

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 债券代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def bond_blk_detail(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取沪深交易所债券大宗交易数据，可以通过

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 债券代码. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def yc_cb(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        curve_type: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        curve_term: float = None,
    ) -> TushareResponse:
        """
        获取中债收益率曲线，目前可获取中债国债收益率曲线即期和到期收益率曲线数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 收益率曲线编码：1001.CB-国债收益率曲线. Defaults to None.
            curve_type (str, optional): 曲线类型：0-到期，1-即期. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 查询起始日期. Defaults to None.
            end_date (str, optional): 查询结束日期. Defaults to None.
            curve_term (float, optional): 期限. Defaults to None.
        """
        pass

    def eco_cal(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        currency: str = None,
        country: str = None,
        event: str = None,
    ) -> TushareResponse:
        """
        获取全球财经日历、包括经济事件数据更新

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期（YYYYMMDD格式）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            currency (str, optional): 货币代码. Defaults to None.
            country (str, optional): 国家（比如：中国、美国）. Defaults to None.
            event (str, optional): 事件 （支持模糊匹配： *非农*）. Defaults to None.
        """
        pass

    def fx_obasic(
        self,
        _fields: list[str] = None,
        *,
        exchange: str = None,
        classify: str = None,
        ts_code: str = None,
    ) -> TushareResponse:
        """
        获取海外外汇基础信息，目前只有FXCM交易商的数据

        Args:
            _fields (list[str], optional): Defaults to None.
            exchange (str, optional): 交易商. Defaults to None.
            classify (str, optional): 分类. Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
        """
        pass

    def fx_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
        exchange: str = None,
    ) -> TushareResponse:
        """
        获取外汇日线行情

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            trade_date (str, optional): 交易日期（GMT，日期是格林尼治时间，比北京时间晚一天）. Defaults to None.
            start_date (str, optional): 开始日期（GMT）. Defaults to None.
            end_date (str, optional): 结束日期（GMT）. Defaults to None.
            exchange (str, optional): 交易商，目前只有FXCM. Defaults to None.
        """
        pass

    def hk_basic(
        self, _fields: list[str] = None, *, ts_code: str = None, list_status: str = None
    ) -> TushareResponse:
        """
        获取港股列表信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): TS代码. Defaults to None.
            list_status (str, optional): 上市状态 L上市 D退市 P暂停上市 ，默认L. Defaults to None.
        """
        pass

    def hk_tradecal(
        self,
        _fields: list[str] = None,
        *,
        start_date: str = None,
        end_date: str = None,
        is_open: str = None,
    ) -> TushareResponse:
        """
        获取交易日历

        Args:
            _fields (list[str], optional): Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            is_open (str, optional): 是否交易 '0'休市 '1'交易. Defaults to None.
        """
        pass

    def hk_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取港股每日增量和历史行情，每日18点左右更新当日数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            trade_date (str, optional): 交易日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def hk_mins(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        freq: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse:
        """
        港股分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码，e.g.00001.HK. Defaults to None.
            freq (str, optional): 分钟频度（1min/5min/15min/30min/60min）. Defaults to None.
            start_date (datetime, optional): 开始日期 格式：2023-03-13 09:00:00. Defaults to None.
            end_date (datetime, optional): 结束时间 格式：2023-03-13 19:00:00. Defaults to None.
        """
        pass

    def us_basic(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        classify: str = None,
        offset: str = None,
        limit: str = None,
    ) -> TushareResponse:
        """
        获取美股列表信息

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            classify (str, optional): 股票分类. Defaults to None.
            offset (str, optional): 开始行数. Defaults to None.
            limit (str, optional): 每页最大行数. Defaults to None.
        """
        pass

    def us_tradecal(
        self,
        _fields: list[str] = None,
        *,
        start_date: str = None,
        end_date: str = None,
        is_open: str = None,
    ) -> TushareResponse:
        """
        获取美股交易日历信息

        Args:
            _fields (list[str], optional): Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            is_open (str, optional): 是否交易. Defaults to None.
        """
        pass

    def us_daily(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        trade_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取美股行情（未复权），包括全部股票全历史行情，以及重要的市场和估值指标

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码（e.g. AAPL）. Defaults to None.
            trade_date (str, optional): 交易日期（YYYYMMDD）. Defaults to None.
            start_date (str, optional): 开始日期（YYYYMMDD）. Defaults to None.
            end_date (str, optional): 结束日期（YYYYMMDD）. Defaults to None.
        """
        pass

    def tmt_twincome(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        item: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取台湾TMT电子产业领域各类产品月度营收数据。

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 报告期. Defaults to None.
            item (str, optional): 产品代码. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
        """
        pass

    def tmt_twincomedetail(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        item: str = None,
        symbol: str = None,
        start_date: str = None,
        end_date: str = None,
        source: str = None,
    ) -> TushareResponse:
        """
        获取台湾TMT行业上市公司各类产品月度营收情况。

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 报告期. Defaults to None.
            item (str, optional): 产品代码. Defaults to None.
            symbol (str, optional): 公司代码. Defaults to None.
            start_date (str, optional): 报告期开始日期. Defaults to None.
            end_date (str, optional): 报告期结束日期. Defaults to None.
            source (str, optional): None. Defaults to None.
        """
        pass

    def bo_monthly(
        self, _fields: list[str] = None, *, date: str = None
    ) -> TushareResponse:
        """
        获取电影月度票房数据

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期（每月1号，格式YYYYMMDD）. Defaults to None.
        """
        pass

    def bo_weekly(
        self, _fields: list[str] = None, *, date: str = None
    ) -> TushareResponse:
        """
        获取周度票房数据

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期（每周一日期，格式YYYYMMDD）. Defaults to None.
        """
        pass

    def bo_daily(
        self, _fields: list[str] = None, *, date: str = None
    ) -> TushareResponse:
        """
        获取电影日度票房

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 （格式YYYYMMDD）. Defaults to None.
        """
        pass

    def bo_cinema(
        self, _fields: list[str] = None, *, date: str = None
    ) -> TushareResponse:
        """
        获取每日各影院的票房数据

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期(格式:YYYYMMDD). Defaults to None.
        """
        pass

    def film_record(
        self,
        _fields: list[str] = None,
        *,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取全国电影剧本备案的公示数据

        Args:
            _fields (list[str], optional): Defaults to None.
            ann_date (str, optional): 公布日期 （至少输入一个参数，格式：YYYYMMDD，日期不连续，定期公布）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def teleplay_record(
        self,
        _fields: list[str] = None,
        *,
        report_date: str = None,
        start_date: str = None,
        end_date: str = None,
        org: str = None,
        name: str = None,
    ) -> TushareResponse:
        """
        获取2009年以来全国拍摄制作电视剧备案公示数据

        Args:
            _fields (list[str], optional): Defaults to None.
            report_date (str, optional): 备案月份（YYYYMM）. Defaults to None.
            start_date (str, optional): 备案开始月份（YYYYMM）. Defaults to None.
            end_date (str, optional): 备案结束月份（YYYYMM）. Defaults to None.
            org (str, optional): 备案机构. Defaults to None.
            name (str, optional): 电视剧名称. Defaults to None.
        """
        pass

    def shibor(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        shibor利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 (日期输入格式：YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def shibor_quote(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        bank: str = None,
    ) -> TushareResponse:
        """
        Shibor报价数据

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 (日期输入格式：YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            bank (str, optional): 银行名称 （中文名称，例如 农业银行）. Defaults to None.
        """
        pass

    def shibor_lpr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        LPR贷款基础利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期  (日期输入格式：YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def libor(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        curr_type: str = None,
    ) -> TushareResponse:
        """
        Libor拆借利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 (日期输入格式：YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            curr_type (str, optional): 货币代码  (USD美元  EUR欧元  JPY日元  GBP英镑  CHF瑞郎，默认是USD). Defaults to None.
        """
        pass

    def hibor(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        Hibor利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期  (日期输入格式：YYYYMMDD，下同). Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def wz_index(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        温州民间借贷利率，即温州指数

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def gz_index(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        广州民间借贷利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
        """
        pass

    def cn_gdp(
        self,
        _fields: list[str] = None,
        *,
        q: str = None,
        start_q: str = None,
        end_q: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取国民经济之GDP数据

        Args:
            _fields (list[str], optional): Defaults to None.
            q (str, optional): 季度（2019Q1表示，2019年第一季度）. Defaults to None.
            start_q (str, optional): 开始季度. Defaults to None.
            end_q (str, optional): 结束季度. Defaults to None.
            fields (str, optional): 指定输出字段（e.g. fields='quarter,gdp,gdp_yoy'）. Defaults to None.
        """
        pass

    def cn_cpi(
        self,
        _fields: list[str] = None,
        *,
        m: str = None,
        start_m: str = None,
        end_m: str = None,
    ) -> TushareResponse:
        """
        获取CPI居民消费价格数据，包括全国、城市和农村的数据

        Args:
            _fields (list[str], optional): Defaults to None.
            m (str, optional): 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔. Defaults to None.
            start_m (str, optional): 开始月份. Defaults to None.
            end_m (str, optional): 结束月份. Defaults to None.
        """
        pass

    def cn_ppi(
        self,
        _fields: list[str] = None,
        *,
        m: str = None,
        start_m: str = None,
        end_m: str = None,
    ) -> TushareResponse:
        """
        获取PPI工业生产者出厂价格指数数据

        Args:
            _fields (list[str], optional): Defaults to None.
            m (str, optional): 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔. Defaults to None.
            start_m (str, optional): 开始月份. Defaults to None.
            end_m (str, optional): 结束月份. Defaults to None.
        """
        pass

    def cn_m(
        self,
        _fields: list[str] = None,
        *,
        m: str = None,
        start_m: str = None,
        end_m: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取货币供应量之月度数据

        Args:
            _fields (list[str], optional): Defaults to None.
            m (str, optional): 月度（202001表示，2020年1月）. Defaults to None.
            start_m (str, optional): 开始月度. Defaults to None.
            end_m (str, optional): 结束月度. Defaults to None.
            fields (str, optional): 指定输出字段（e.g. fields='month,m0,m1,m2'）. Defaults to None.
        """
        pass

    def sf_month(
        self,
        _fields: list[str] = None,
        *,
        m: str = None,
        start_m: str = None,
        end_m: str = None,
    ) -> TushareResponse:
        """
        获取月度社会融资数据

        Args:
            _fields (list[str], optional): Defaults to None.
            m (str, optional): 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔. Defaults to None.
            start_m (str, optional): 开始月份. Defaults to None.
            end_m (str, optional): 结束月份. Defaults to None.
        """
        pass

    def us_tycr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取美国每日国债收益率曲线利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 （YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定输出字段（e.g. fields='m1,y1'）. Defaults to None.
        """
        pass

    def us_trycr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        国债实际收益率曲线利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期 （YYYYMMDD格式，下同）. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定输出字段. Defaults to None.
        """
        pass

    def us_tbr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        获取美国短期国债利率数据

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期(YYYYMMDD格式). Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定输出字段(e.g. fields='w4_bd,w52_ce'). Defaults to None.
        """
        pass

    def us_tltr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        国债长期利率

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定字段. Defaults to None.
        """
        pass

    def us_trltr(
        self,
        _fields: list[str] = None,
        *,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        fields: str = None,
    ) -> TushareResponse:
        """
        国债实际长期利率平均值

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期. Defaults to None.
            start_date (str, optional): 开始日期. Defaults to None.
            end_date (str, optional): 结束日期. Defaults to None.
            fields (str, optional): 指定字段. Defaults to None.
        """
        pass

    def news(
        self,
        _fields: list[str] = None,
        *,
        start_date: datetime = None,
        end_date: datetime = None,
        src: str = None,
    ) -> TushareResponse:
        """
        获取主流新闻网站的快讯新闻数据

        Args:
            _fields (list[str], optional): Defaults to None.
            start_date (datetime, optional): 开始日期. Defaults to None.
            end_date (datetime, optional): 结束日期. Defaults to None.
            src (str, optional): 新闻来源 见下表. Defaults to None.
        """
        pass

    def major_news(
        self,
        _fields: list[str] = None,
        *,
        src: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取长篇通讯信息，覆盖主要新闻资讯网站

        Args:
            _fields (list[str], optional): Defaults to None.
            src (str, optional): 新闻来源. Defaults to None.
            start_date (str, optional): 新闻发布开始时间，e.g. 2018-11-21 00:00:00. Defaults to None.
            end_date (str, optional): 新闻发布结束时间，e.g. 2018-11-22 00:00:00. Defaults to None.
        """
        pass

    def cctv_news(
        self, _fields: list[str] = None, *, date: str = None
    ) -> TushareResponse:
        """
        获取新闻联播文字稿数据，数据开始于2006年6月，超过12年历史

        Args:
            _fields (list[str], optional): Defaults to None.
            date (str, optional): 日期（输入格式：YYYYMMDD 比如：20181211）. Defaults to None.
        """
        pass

    def anns_d(
        self,
        _fields: list[str] = None,
        *,
        ts_code: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取全量公告数据，提供pdf下载URL

        Args:
            _fields (list[str], optional): Defaults to None.
            ts_code (str, optional): 股票代码. Defaults to None.
            ann_date (str, optional): 公告日期（yyyymmdd格式，下同）. Defaults to None.
            start_date (str, optional): 公告开始日期. Defaults to None.
            end_date (str, optional): 公告结束日期. Defaults to None.
        """
        pass

    def ncov_num(
        self,
        _fields: list[str] = None,
        *,
        area_name: str = None,
        level: str = None,
        ann_date: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> TushareResponse:
        """
        获取新冠状肺炎疫情感染人数统计数据

        Args:
            _fields (list[str], optional): Defaults to None.
            area_name (str, optional): 地区名称. Defaults to None.
            level (str, optional): 级别：2-中国内地，3-省级，4-地区市级别. Defaults to None.
            ann_date (str, optional): 公告日期. Defaults to None.
            start_date (str, optional): 查询开始日期. Defaults to None.
            end_date (str, optional): 查询结束日期. Defaults to None.
        """
        pass

    def ncov_global(
        self,
        _fields: list[str] = None,
        *,
        country: str = None,
        province: str = None,
        publish_date: datetime = None,
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> TushareResponse:
        """
        获取全球新冠疫情数据，包括国家和地区

        Args:
            _fields (list[str], optional): Defaults to None.
            country (str, optional): 国家名称. Defaults to None.
            province (str, optional): 省份简称（北京、上海）. Defaults to None.
            publish_date (datetime, optional): 公布日期. Defaults to None.
            start_date (datetime, optional): 开始日期（YYYYMMDD）. Defaults to None.
            end_date (datetime, optional): 结束日期（YYYYMMDD）. Defaults to None.
        """
        pass

    def fund_sales_ratio(
        self, _fields: list[str] = None, *, 年份: str = None
    ) -> TushareResponse:
        """
        获取各渠道公募基金销售保有规模占比数据，年度更新

        Args:
            _fields (list[str], optional): Defaults to None.
            年份 (str, optional): 年度. Defaults to None.
        """
        pass

    def fund_sales_vol(
        self,
        _fields: list[str] = None,
        *,
        year: str = None,
        quarter: str = None,
        name: str = None,
    ) -> TushareResponse:
        """
        获取销售机构公募基金销售保有规模数据，本数据从2021年Q1开始公布，季度更新

        Args:
            _fields (list[str], optional): Defaults to None.
            year (str, optional): 年度. Defaults to None.
            quarter (str, optional): 季度. Defaults to None.
            name (str, optional): 机构名称. Defaults to None.
        """
        pass


class TushareProAPI(TushareProAPIBase, DataSource):
    _token: str
    _base_url: str
    _timeout: int

    def __init__(
        self, token: str, *, base_url: str = "http://api.waditu.com", timeout: int = 30
    ):
        self._token = token
        self._base_url = base_url
        self._timeout = timeout
        super().__init__()

    def _run_query(
        self, api_name: str, _fields: list[str] = None, **kwargs
    ) -> TushareResponse:
        if not _fields:
            _fields = []
        req_params = {
            "api_name": api_name,
            "token": self._token,
            "params": kwargs,
            "fields": ",".join(_fields),
        }
        with self.session.post(
            self._base_url, json=req_params, timeout=self._timeout
        ) as res:
            result: dict = res.json()
            if result["code"] != 0:
                raise TushareResponseError(**result)
            return TushareResponse(**result)

    def __getattribute__(self, item):
        if not item.startswith("_") and hasattr(TushareProAPIBase, item):
            return partial(self._query, item)
        return object.__getattribute__(self, item)
