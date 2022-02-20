# -*- coding: utf-8 -*-
"""
@File    : 测试json.py
@Time    : 2021/12/28 13:34
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import json

p = '''
{
            compatible: true,
            product: {
                modules: [
                    'address',
                    'prom',
                    'colorsize',
                    'buytype',
                    'baitiao',
                    'jincai',
                                        'summary',
                    'o2o',
                    'buybtn',
                    'track',
                    'suits',
                    'crumb',
                    'fittings',
                    'detail',
                    'contact',
                    'popbox',
                    'preview',
                    'info',
                    'imcenter',
                    'jdservice',
                    'jdservicePlus',
                    'jdserviceF',
                    'ycservice',
                    'commitments',
                    'gift',
                                                                                                        'vehicle'                ],
                            imageAndVideoJson: {"mainVideoId":"579849529"},
                         authors: [],             ostime: 1640666252.912,
            skuid: 10031792658506,
        skuMarkJson: {"isxg":false,"isJDexpress":false,"isrecyclebag":false,"isSds":false,"isSopJSOLTag":false,"isyy":false,"isPOPDistribution":false,"isSopUseSelfStock":false,"isGlobalPurchase":false,"NosendWMS":false,"isOripack":false,"ispt":false,"unused":false,"pg":false,"isSopWareService":false,"isTimeMark":false,"presale":false},
            name: '惠普（HP）光影精灵7Victus游戏电竞性能直播吃鸡笔记本电脑暗影精灵11代酷睿独显高色域背光键盘 RTX3050/i5-11400H/高色域',
            skuidkey:'C28BD495DB5DA6ADB81FA15CED8257487B46AAEA22E18860',
            href: '//item.jd.com/10031792658506.html',
                            fsEndOffset:40948000,fsEndTime:1640707200000,
                        src: 'jfs/t1/217970/15/7709/116893/61b84102E5b97a46d/71751fd31d78b94c.jpg',
            paramJson: '{"platform2":"1","colType":100,"specialAttrStr":"p0pppp1ppppp2pppppppppppp","skuMarkStr":"00"}' ,
                            imageList: ["jfs/t1/217970/15/7709/116893/61b84102E5b97a46d/71751fd31d78b94c.jpg","jfs/t1/84859/12/15346/96493/61400893E97761dfc/b159cfa5294dfcde.jpg","jfs/t1/187339/17/14876/236218/60fd2a3dEb8e85e7b/7ea6cc600eda9773.png","jfs/t1/195851/12/7312/86729/60c05fbcEb68e30db/8fd6bc9c1c45b6cb.jpg","jfs/t1/172911/32/13897/85656/60c05fbcE9e9d708e/3ca7ca35389482e8.jpg","jfs/t1/175118/7/13778/87223/60c05fbcE1695a36a/e7d8762a219b0deb.jpg","jfs/t1/186917/7/7270/77771/60c05fbcEe36b56ab/b39af16cb2dc77d9.jpg","jfs/t1/193437/8/7204/72815/60c05fbcEbf428e87/3fa595c6c209a8ab.jpg","jfs/t1/185903/19/8101/78159/60c05fbdE84f4487e/ba88f10705c4fbc7.jpg"],
                        cat: [670,671,1105],
            forceAdUpdate: '8274',
        catName: ["电脑、办公","电脑整机","游戏本"],        brand: 8740,
        pType: 1,
        isClosePCShow: false,
         pTag:10000930,                                                 isPop:false,
        isSelf:false,
        venderId:10171379,
        shopId:'10037291',
        isQualityLifeShow:true,
        shopSwitch:true,
        freeBuyShow:false,
                                                specialAttrs:["isPrescriptCat-0","thwa-3","isFlashPurchase-2","nationallySetWare-2","IsJDMarket-1","is7ToReturn-1","isOTCCat-0"],
                recommend : [0,1,2,3,4,5,6,7,8,9],
        easyBuyUrl:"//easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action",
        qualityLife: "//c.3.cn/qualification/info?skuId=10031792658506&pid=10021086935136&catId=1105",
                colorSize: [{"skuId":10031792658506,"处理器或显卡":"RTX3050/i5-11400H/高色域"},{"skuId":10031792658507,"处理器或显卡":"RTX3060/i7-11800H/144Hz"},{"skuId":10031792658508,"处理器或显卡":"RTX3050Ti/i7-11800H/高色域"},{"skuId":10035230636226,"处理器或显卡":"RTX3050Ti/i5-11400H/高色域"},{"skuId":10035977770999,"处理器或显卡":"RTX3050/i7-11800H/高色域"},{"skuId":10037132164770,"处理器或显卡":"RTX3060/i5-11400H/144Hz"},{"skuId":10038572269694,"处理器或显卡":"GTX1650/i5-11400H/高色域"}],        warestatus: 1,                                 desc: '//cd.jd.com/description/channel?skuId=10031792658506&mainSkuId=10021086935136&charset=utf-8&cdn=2',
        cmsNavigation: [{"address":"//channel.jd.com/670-671.html","order":1,"name":"电脑办公","corner":""},{"address":"//intelrxt.jd.com/","order":2,"name":"用芯选机","corner":""},{"address":"//gaming.jd.com/","order":3,"name":"京东游戏","corner":""},{"address":"//jdz.jd.com/","order":4,"name":"电脑私人定制","corner":""},{"address":"//channel.jd.com/670-671.html","order":5,"name":"本周热卖","corner":""},{"address":"//sale.jd.com/act/F5ZurL6zbcN.html","order":6,"name":"吃鸡利器","corner":"优惠多"}],        /**/
                 /**/
                twoColumn: true,                isFeeType: true,                                        isBookMvd4Baby: false,                        addComments:true,
        mainSkuId:'10021086935136',        foot: '//dx.3.cn/footer?type=common_config2',
                fcs: true,                   shangjiazizhi: false        }
        }
'''

print(p.replace('\'','"'))